#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/17 16:13
# @Author  :  wancheng.b
# @Site     : 
# @File     : Driver.py
# @Software  : PyCharm
import subprocess
import threading
import time
from multiprocessing.pool import Pool
import public.LogUtils as U
# from po.BasePage import BasePage
from po.BasePage import BasePage
from public.FileOperate import mkdir_file
from public.RunCases import RunCases


@U.l()
def getDevices():
    '''
    换行分割截取掉头和尾，然后用\T（Tab）截取
    :return: devices_list
    '''

    devices = []
    devicesName = subprocess.getoutput('adb devices')
    devicesName = devicesName.split("\n")[1: -1]
    for deviceName in devicesName:
        deviceName = deviceName.split('\tdevice')
        devices.append(deviceName[0])
    #     用ip连接的时候会device是有ip+：port合成的，生成u2对象的时候只用到ip所以把：和port删除掉就好了
    for device in devices:
        if device.find(':') != -1:
            devices.append(device.split(':')[0])
            devices.remove(device)
    if len(devices) > 0:
        return devices
    else:
        U.Logging.warn('设备未连接')


class Driver:
    def __init__(self):
        pass

    @staticmethod
    def runCases(deviceObj):
        page = BasePage()
        page.set_driver(deviceObj.get_device())
        page.get_driver().shell('logcat -c')
        time.sleep(1)
        deviceObj.unittest_run()
        page.get_driver().shell('logcat -d > /sdcard/logcat.txt')
        page.get_driver().pull('/sdcard/logcat.txt',
                               '{}\log\logcat.txt'.format(deviceObj.result_path))

    def runAllCases(self):
        devices_list = getDevices()
        # 创建所有RunCases对象,存入driver_list
        driver_list = []
        for device in devices_list:
            result_path = mkdir_file(device)
            driver_list.append(RunCases(device, result_path))
        pool = Pool(processes=len(driver_list))
        for deviceObj in driver_list:
            pool.apply_async(self.runCases,
                             args=(deviceObj,))
        print('Waiting for all runs done........ ')
        pool.close()
        pool.join()
        print('All runs done........ ')


if __name__ == '__main__':
    getDevices()

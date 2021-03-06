#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/5/5 10:40
# @Author  :  wancheng.b
# @Site     :
# @File     : Sale200_test.py
# @Software  : PyCharm
import time
import unittest

from lib.adbUtils import ADB
from po.BasePage import BasePage
from po.Page import PagePo
from po.Process import Process
import uiautomator2 as u2

from public import HTMLTestReport
from public.FileOperate import getTest_info
from public.LogUtils import Logging


class MyTestCase(unittest.TestCase, BasePage):
    '''
    tearDown()和setUp()是每执行一个TestCase都会执行
    setUpClass()和tearDownClass()每个文件执行前和结束会执行

    '''

    @classmethod
    def setUpClass(cls):
        Process.testInit()

    def test_Sale200(self):
        driver = u2.connect('10.172.24.71')
        package_name = getTest_info('test_package_name', 'package_name')
        test_ScbQR_path = 'D:\pycharm\PycharmWorkSpase\AtxMultidevice\yamlsTestCase\Sale200Tester\Sale200.yaml'
        page = PagePo(driver, test_ScbQR_path)
        driver.shell('logcat -c')
        time.sleep(1)
        Logging.info('电池电量：' + str(ADB().get_battery_level()))
        Logging.info('磁盘信息' + str(ADB().get_disk()))
        # page.main()
        num = 2
        for i in range(num):
            # 单个用例执行次数
            page.main()
            # # 返回主页面从头开始
            driver.session(package_name)

        CPURate = ADB().get_cpu(package_name)
        Logging.info('CPU使用率为' + str(CPURate))
        Logging.info('电池电量：' + str(ADB().get_battery_level()))
        Logging.info('磁盘信息' + str(ADB().get_disk()))
        driver.shell('logcat -d > /sdcard/logcat.txt')
        driver.pull('/sdcard/logcat.txt',
                    'D:\pycharm\PycharmWorkSpase\AtxMultidevice\logcat.txt')

    @classmethod
    def tearDownClass(cls):
        Process.testEnd()


if __name__ == '__main__':
    # unittest.main()

    # 添加一个测试用例
    suite = unittest.TestSuite()
    # 添加Single01Test模块下的SingleTest类的test_first测试用例
    # suite.addTest(Single01Test.Single01Test('test_first'))
    # 可以添加多次同一个案例
    suite.addTest(MyTestCase('test_Sale200'))
    # suite.addTest(Single02Test.MyTestCase('test_something'))
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity控制输出的执行结果的详细程度，可为0，1，2，其中0最简单，1是默认值，2最详细
    runner.run(suite)
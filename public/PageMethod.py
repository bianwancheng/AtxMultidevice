# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     PageMethod
   Description :
   Author :       bianwancheng
   date：          2019/3/18
-------------------------------------------------
   Change Activity:
                   2019/3/18:
-------------------------------------------------
__author__ = 'wancheng.b'
"""
import os
import time

import yaml
from public import LogUtils

from public.FileOperate import getTest_info
from public.LogUtils import Logging

'''
resultReport路径
'''


def getReportPath():
    result_path = getTest_info('test_case', 'log_file')
    dir_list = os.listdir(result_path)[-1]
    result_path = result_path + '/' + dir_list
    return result_path


'''
解析yaml，return：dict
'''


@LogUtils.l()
def getYaml(path):
    with open(path, 'r', encoding='utf-8')as f:
        deviceYaml = yaml.load(f)
    return deviceYaml


'''
给页面操作加装饰器（点击，滑动等等）
带参数的装饰器装饰带参数的函数
path：截屏存储地址
'''


def operateDecorate():
    def Decorate(func):
        """
            打印log
            文件名+函数名,return
            :return:
            """

        def operate(arg, *args):
            try:
                func(arg, *args)
            except:
                date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
                screenShot = date_time + '_' + list(*args)[0] + '.PNG'
                path = getReportPath() + '\img' + '\\' + screenShot
                arg.screenshot(path)
                # Logging.debug('raise Exception screenShot')
                raise Exception('IMAGE:' + screenShot)

        return operate

    return Decorate


'''
@ description 通过X, Y 坐标滑动

'''


@operateDecorate()
def scrollByXY(driver, elementList):
    pass


'''
@ description 通过X, Y 坐标点击
@:parameter driver, elementinfo_List

'''


@operateDecorate()
def clickByXY(driver, element_list):
    try:
        driver.click(element_list[0], element_list[1])
        Logging.success('driver click' + str(element_list) + 'success by XY')
    except Exception as e:
        raise e


'''
@description 通过text点击
@:parameter driver, elementinfo_List
'''


@operateDecorate()
def clickByText(driver, element_list):
    clicked = driver(text=element_list[0]).click_exists(timeout=int(element_list[1]))  # return bool
    if clicked:
        driver(text=element_list[0]).click(timeout=int(element_list[1]))
        Logging.success('driver click' + element_list[0] + 'success by Text')
    else:
        Logging.error('no found' + element_list[0])


if __name__ == '__main__':
    '''d = u2.connect('55cac15d')
    d.app_start('com.test.ui.activities.nihao')
    list = ['测试工具', 10]
    clickByText(d, list)
    print('装饰器没有问题')
    '''
    pass

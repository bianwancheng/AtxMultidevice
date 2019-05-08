#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/13 16:12
# @Author  :  wancheng.b
# @Site     : 
# @File     : Process.py
# @Software  : PyCharm

import os
from lib.adbUtils import ADB
from po.Driver import getDevices
from public.LogUtils import Logging
import warnings
from public.FileOperate import getTest_info


class Process:

    @classmethod
    def testInit(cls):

        '''
                安装atx和apk

                :return:
                '''
        warnings.simplefilter('ignore', ResourceWarning)
        package_name = getTest_info('test_package_name', 'package_name')
        package_atx = getTest_info('test_package_name', 'package_atx')
        if not ADB().is_install(package_name):
            ADB().install_app(getTest_info('test_package_name', 'package_name_path'))
            Logging.info('install' + package_name + 'success')

        if not ADB().is_install(package_atx):
            os.system('python -m uiautomator2 init')
            Logging.info('install' + package_atx + 'success')
        else:
            pass


    @classmethod
    def testEnd(cls):
        # 退出app，返回apk主页面
        ADB().quit_app(getTest_info('test_package_name', 'package_name'))
        # ADB().start_activity('com.android.launcher3/.Launcher')





if __name__ == '__main__':
    Process.testEnd()

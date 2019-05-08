# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RunOneCase.py
   Description :
   Author :       bianwancheng
   date：          2019/3/18
-------------------------------------------------
   Change Activity:
                   2019/3/18:
-------------------------------------------------
__author__ = 'wancheng.b'
"""

from po.Driver import Driver
from public.LogUtils import Logging
from public.FileOperate import getTest_info, existCase
from public.chromedriver import ChromeDriver

if __name__ == '__main__':
    if len(existCase(getTest_info('test_case', 'caseYaml'))) > 0:
        Driver().runAllCases()
        ChromeDriver.kill()
    else:
        Logging.error("测试案例不存在")
    pass

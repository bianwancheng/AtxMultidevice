#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/12 14:43
# @Author  :  wancheng.b
# @Site     : 
# @File     : TestSuit.py
# @Software  : PyCharm

# 构造测试集
import os
import unittest

from TestCase.TestSuit import Single01Test, Single02Test
from public import HTMLTestReport

case_path = os.getcwd()  # case所在路径
# 添加一个测试用例
suite = unittest.TestSuite()
# 添加Single01Test模块下的SingleTest类的test_first测试用例
# suite.addTest(Single01Test.Single01Test('test_first'))
# 可以添加多次同一个案例
suite.addTest(Single02Test.MyTestCase('test_something'))
suite.addTest(Single02Test.MyTestCase('test_something'))
runner = unittest.TextTestRunner(verbosity=2)  # verbosity控制输出的执行结果的详细程度，可为0，1，2，其中0最简单，1是默认值，2最详细
runner.run(suite)



# print(discover)
# discover相当于在指定的case所在的路径里寻找所有名称模式匹配pattern的文件并加载其内容，相当于suite的集合
# case_path = os.getcwd()  # case所在路径
# discover = unittest.defaultTestLoader.discover(case_path, pattern="*Test.py")
# runner = unittest.TextTestRunner(verbosity=2)  # verbosity控制输出的执行结果的详细程度，可为0，1，2，其中0最简单，1是默认值，2最详细
# runner.run(discover)
# html文件存放路径


# case_path = os.getcwd()  # case所在路径
# discover = unittest.defaultTestLoader.discover(case_path, pattern="*Test.py")
# fp = open('D:\pycharm\PycharmWorkSpase\AtxMultidevice\TestCase\TestSuit\\result.html', "wb")
# runner = HTMLTestReport.HTMLTestRunner(stream=fp,
#                                            title=u'自动化测试报告,测试结果如下：',
#                                            description=u'用例执行情况：')
# runner.run(discover)
# fp.close()


# if __name__ == '__main__':
#     print(case_path)
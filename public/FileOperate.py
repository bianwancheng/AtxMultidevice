#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/11 10:39
# @Author  :  wancheng.b
# @Site     : 
# @File     : FileOperate.py
# @Software  : PyCharm
import configparser
import os
import random
import time
from public.LogUtils import Logging


'''
获取test_info.ini section下面的key对应的value值
'''


def getTest_info(section, key):
    try:
        config = configparser.ConfigParser()
        config.read('D:\pycharm\PycharmWorkSpase\AtxMultidevice\data\\test_info.ini', encoding='utf-8')
        return config.get(section, key)
    except Exception as e:
        Logging.error('test_info.ini路径错误:{}'.format(e))
        raise e


'''
测试案例是否存在return caseDirList
'''


def existCase(path):
    if os.path.exists(path):
        caseList = []
        for dirpath, dirname, files in os.walk(path):
            for file in files:
                # print(os.path.join(dirpath, file))
                caseList.append(os.path.join(dirpath, file))
        # Logging.info('测试案例共有' + str(len(caseList)) + '个，' + '用例路径：' + path)
        return caseList
    else:
        Logging.error('测试案例路径不存在')


'''
得到测试用例yaml的路径
路径的问题有点疑问，相对路径的问题
'''


def getOneCaseYamlPath(Tester, caseYaml):
    rootpath = os.path.abspath('.')
    Logging.debug(rootpath)
    caseYamlPath = rootpath + '\\yamlsTestCase\\' + Tester + '\\' + caseYaml
    return caseYamlPath


def mkdir_file(device):
    """

    :return:创建日志存放文件夹
    """
    # 如果用ip连接的时候device类似：10.172.24.79:5555，'：'号在创建文件夹的时候是不被允许的，所以替换成'_'
    if str(device).find(':'):
        device = str(device).replace(':', '_')
    else:
        pass
    result_file = getTest_info('test_case', 'log_file')
    result_file_every = result_file + '/' + \
                        time.strftime("%Y-%m-%d_%H_%M_%S{}".format(random.randint(10, 99)),
                                      time.localtime(time.time())) + '_' + device
    file_list = [
        result_file,
        result_file_every,
        result_file_every + '/log',
        result_file_every + '/html',
        result_file_every + '/img',
    ]
    if not os.path.exists(result_file):
        os.mkdir(result_file)

    for file_path in file_list:
        if not os.path.exists(file_path):
            os.mkdir(file_path)
    return result_file_every


if __name__ == '__main__':
    mkdir_file('10.172.24.79:5555')
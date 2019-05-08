#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/13 16:44/
# @Author  :  wancheng.b
# @Site     : 
# @File     : AnylizeYaml.py
# @Software  : PyCharm

import yaml
from yaml.scanner import ScannerError
import os

'''
返回一个flag和yaml列表
paremeter:filePath
'''
def getYam(path):
    try:
        with open(path, encoding='utf-8') as f:
            x = yaml.load(f)
            return [True, x]
    except FileNotFoundError:
        print("==用例文件不存在==")
        app = {'check': [{'element_info': '', 'operate_type': 'get_value', 'find_type': 'ids', 'info': '用例文件不存在'}],
               'testinfo': [{'title': '', 'id': '', 'info': '', "msg": ""}],
               'testcase': [{'element_info': '', 'info': '', 'operate_type': '', 'find_type': ''},
                            {'element_info': '', 'msg': "", 'operate_type': '', 'find_type': '', 'info': ''},
                            {'element_info': '', 'msg': '', 'operate_type': '', 'find_type': '', 'info': ''},
                            {'element_info': '', 'info': '', 'operate_type': '', 'find_type': ''}]}

        return [False, app]
    except yaml.scanner.ScannerError:
        app = {'check': [{'element_info': '', 'operate_type': 'get_value', 'find_type': 'ids', 'info': '用例文件格式错误'}],
               'testinfo': [{'title': '', 'id': '', 'info': '', "msg": " "}],
               'testcase': [{'element_info': '', 'info': '', 'operate_type': '', 'find_type': ''},
                            {'element_info': '', 'msg': "", 'operate_type': '', 'find_type': '', 'info': ''},
                            {'element_info': '', 'msg': '', 'operate_type': '', 'find_type': '', 'info': ''},
                            {'element_info': '', 'info': '', 'operate_type': '', 'find_type': ''}]}
        print("==用例格式错误==")
        return [False, app]
    except Exception as e:
        print(path + "yaml文件错误，具体不知")
        raise e


if __name__ == '__main__':
    import os

    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    # 感觉没啥意义还不如直接写绝对路径
    # print(os.path.dirname("../yamls/home/firstOpen.yaml"))
    # print(PATH("../yamls/home/firstOpen.yaml"))
    t = getYam(PATH("../yamls/Home/home01.yaml"))
    print(t)
    # print(type(t))
    # print(type(t[1]['testcase']))
    # print(t)



# -*- coding: utf-8 -*-

import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录的子文件


# 创建目录
def mkdirPath(path):
    if not os.path.exists(path):
        os.mkdir(path)
    list = ['log', 'img']
    for i in list:
        os.mkdir(os.path.join(path, i))


'''
其实os.path.dirname()就是返回上级目录的意思，如果传的参数是个文件，那么就返回当前文件所在目录，如果传的参数是个文件目录，
那么就返回这个目录的上级目录。 os.path.dirname(arg)
para:str
'''


def dirname(arg):
    return os.path.dirname(arg)


'''
返回当前目录 os.getcwd()
'''


def getcwd():
    return os.getcwd()


'''
获取当前文件的绝对路径  os.path.abspath(arg)
para:str
'''


def getAbsPath(arg):
    return os.path.abspath(arg)


'''
拼接路径 os.path.join(path, *name)
para：路径、文件名（可以是多个）
'''


def getJoinPat(path, *name):
    return os.path.join(path, *name)

'''
指定目录下所有文件,不包括子目录下的 os.listdir(“dirname”)
'''

def getListDir(dirname):
    return os.listdir(dirname)

if __name__ == '__main__':
    # __file__是内置变量，代表的就是当前运行的程序文件
    # print(dirname(__file__))  # 但是这里如果写的是test.py返回的是空串
    # print(dirname('D:\pycharm\PycharmWorkSpase\AtxMultidevice\TestCase\TestSuit\Single02Test.py'))
    # print(getcwd())
    # print(getAbsPath(__file__))  # 这里如果写的是test.p没有问题
    # print('-----------------------------------')
    # dirname = dirname(__file__)
    # print(dirname)
    # print(getJoinPat(dirname, 'dsd', 'dg'))
    # print(getListDir('D:\pycharm\PycharmWorkSpase\AtxMultidevice\TestCase\TestSuit'))
    mkdirPath('D:\pycharm\PycharmWorkSpase\AtxMultidevice\\testNode\\result')

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RunOneCase.py
   Description :
   Author :       bianwancheng
   date：          2019/3/27
-------------------------------------------------
   Change Activity:
                   2019/3/27:
-------------------------------------------------
__author__ = 'wancheng.b'
"""
import sys
import time


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


class colour:
    @staticmethod
    def c(msg, colour):
        try:
            from termcolor import colored, cprint
            p = lambda x: cprint(x, '%s' % colour)
            return p(msg)
        except:
            print(msg)

    @staticmethod
    def show_verbose(msg):
        colour.c(msg, 'white')

    @staticmethod
    def show_debug(msg):
        colour.c(msg, 'blue')

    @staticmethod
    def show_info(msg):
        colour.c(msg, 'green')

    @staticmethod
    def show_warn(msg):
        colour.c(msg, 'yellow')

    @staticmethod
    def show_error(msg):
        colour.c(msg, 'red')


def l():
    """
    打印log
    文件名+函数名,return
    :return:
    """

    def log(func):
        def wrapper(*args, **kwargs):
            t = func(*args, **kwargs)
            filename = str(sys.argv[0]).split('/')[-1].split('.')[0]
            Logging.success('{}:{}, return:{}'.format(filename, func.__name__, t))
            return t

        return wrapper

    return log


class Logging:
    flag = True

    @staticmethod
    def error(msg):
        if Logging.flag:
            colour.show_error(get_now_time() + " [Error]:" + "".join(msg))

    @staticmethod
    def warn(msg):
        if Logging.flag:
            colour.show_warn(get_now_time() + " [Warn]:" + "".join(msg))

    @staticmethod
    def info(msg):
        if Logging.flag:
            colour.show_info(get_now_time() + " [Info]:" + "".join(msg))

    @staticmethod
    def debug(msg):
        if Logging.flag:
            colour.show_debug(get_now_time() + " [Debug]:" + "".join(msg))

    @staticmethod
    def success(msg):
        if Logging.flag:
                colour.show_verbose(get_now_time() + " [Success]:" + "".join(msg))


if __name__ == '__main__':
    pass

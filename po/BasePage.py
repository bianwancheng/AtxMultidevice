#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/17 16:10
# @Author  :  wancheng.b
# @Site     :
# @File     : BasePage.py
# @Software  : PyCharm

import uiautomator2 as u2

class BasePage(object):
    @classmethod
    def set_driver(cls, dri):
        cls.d = u2.connect(dri)


    def get_driver(self):
        return self.d



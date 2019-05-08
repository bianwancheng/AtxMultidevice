#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/12 14:06
# @Author  :  wancheng.b
# @Site     :
# @File     : Single01Test.py
# @Software  : PyCharm
import time
import unittest


class Single01Test(unittest.TestCase):
    def test_first(self):
        print('123')
        # self.assertEqual(True, True)

    @classmethod
    def tearDownClass(cls):
        print('Single01Test.py over')


if __name__ == '__main__':
    unittest.main()

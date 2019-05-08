# import unittest
# from po.BasePage import BasePage
# from po.Page import PagePo
# from po.Process import Process
# from public.FileOperate import getOneCaseYamlPath
#
#
# class MyTestCase(unittest.TestCase, BasePage):
#
#     '''
#     tearDown()和setUp()是每执行一个TestCase都会执行
#     setUpClass()和tearDownClass()每个文件执行前和结束会执行
#
#     '''
#
#     @classmethod
#     def setUpClass(cls):
#         Process.testInit()
#
#     def test_Sale200(self):
#         test_ScbQR_path = getOneCaseYamlPath('Sale200Tester', 'Sale200.yaml')
#         page = PagePo(self.get_driver(), test_ScbQR_path)
#         for i in range(2):  # 可以控制同一个yaml文件执行次数
#             page.main()
#
#     @classmethod
#     def tearDownClass(cls):
#         Process.testEnd()
#
#
# if __name__ == '__main__':
#     unittest.main()

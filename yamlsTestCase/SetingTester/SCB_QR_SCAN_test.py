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
#     def test_scbQR(self):
#         test_ScbQR_path = getOneCaseYamlPath('SetingTester', 'SCB_QR_SCAN.yaml')
#         page = PagePo(self.get_driver(), test_ScbQR_path)
#         page.main()
#         # 手动截屏
#         # u2.connect(device).screenshot()
#
#     @classmethod
#     def tearDownClass(cls):
#         Process.testEnd()
#
#
# if __name__ == '__main__':
#     unittest.main()

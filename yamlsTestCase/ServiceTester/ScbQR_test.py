import unittest
from po.BasePage import BasePage
from po.Page import PagePo
from po.Process import Process
from public.FileOperate import getOneCaseYamlPath


class MyTestCase(unittest.TestCase, BasePage):


    @classmethod
    def setUpClass(cls):
        Process.testInit()

    def test_scbQR(self):
        test_ScbQR_path = getOneCaseYamlPath('ServiceTester', 'ScbQR.yaml')
        page = PagePo(self.get_driver(), test_ScbQR_path)
        page.main()
        # 手动截屏
        # self.d.screenshot()

    @classmethod
    def tearDownClass(cls):
        Process.testEnd()


if __name__ == '__main__':
    unittest.main()

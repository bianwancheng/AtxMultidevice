import unittest
from public import HTMLTestReport
from public.FileOperate import getTest_info

class RunCases:
    def __init__(self, device, result_path):
        self.device = device
        self.result_path = result_path

    def get_device(self):
        return self.device

    def unittest_run(self):
        process_path = getTest_info('test_case', 'caseYaml')
        discover = unittest.defaultTestLoader.discover(process_path,
                                                       pattern="*test.py")
        html_path = self.result_path + '\html' + '\\result.html'
        fp = open(html_path, "wb")
        runner = HTMLTestReport.HTMLTestRunner(stream=fp,
                                               title=u'自动化测试报告,测试结果如下：',
                                               description=u'用例执行情况：')
        # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='da', description='df')
        runner.run(discover)
        fp.close()


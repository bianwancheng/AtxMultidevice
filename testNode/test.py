import csv
import subprocess
import time
import unittest
import uiautomator2 as u2
import warnings


class ADB(object):
    """
    单个设备，可不传入参数device_id
    """

    def __init__(self, device_id=""):
        if device_id == "":
            self.device_id = ""
        else:
            # adb -s 设备号 命令  指定设备执行命令   adb -s as23525 logcat - v
            self.device_id = "-s %s" % device_id

    def adb(self, args):
        cmd = "%s %s %s" % ('adb', self.device_id, str(args))
        return subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def shell(self, args):
        cmd = "%s %s shell %s" % ('adb', self.device_id, str(args),)
        return subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def get_disk(self):
        """
        获取手机磁盘信息
        :return: Used:用户占用,Free:剩余空间
        """
        for s in self.shell('df').stdout.readlines():
            if '/mnt/shell/emulated' in str(s) or '/storage/sdcard0' in str(s):
                lst = []
                for i in str(s.strip()).split(' '):
                    if i:
                        lst.append(i)
                return 'Used:%s,Free:%s' % (lst[2], lst[3])

    def get_battery_level(self):
        """
        获取电池电量
        """
        level = str(self.shell("dumpsys battery | findstr level"
                               ).stdout.read().strip(), encoding='utf-8').split(": ")[-1]

        return int(level)

    def get_cpu(self, package_name):
        """
        获取当前cpu百分比
        """
        p = self.shell(
            'top -n 1 -d 0.5 | findstr %s' %
            (package_name))
        while True:
            r = p.stdout.readline().strip().decode('utf-8')
            if r.endswith(package_name):
                lst = [cpu for cpu in r.split(' ') if cpu]
                return int(lst[2].split('%', 1)[0])

    def quit_app(self, package_name):
        """
        退出app，类似于kill掉进程
        usage: quitApp("com.android.settings")
        """
        self.shell("am force-stop %s" % package_name)

    def get_app_start_total_time(self, component):
        """
        获取启动应用所花时间
        usage: getAppStartTotalTime("com.android.settings/.Settings")
        """
        time = str(self.shell("am start -W %s | findstr TotalTime" %
                              (component)).stdout.read(), encoding='utf-8').split(": ")[-1]
        return int(time)

    def clear_app_data(self, packageName):
        """
        清除应用用户数据
        usage: clearAppData("com.android.contacts")
        """
        if "Success" in self.shell(
                "pm clear %s" %
                packageName).stdout.read().splitlines():
            return "clear user data success "
        else:
            return "make sure package exist"

    def get_network_state(self):
        """
        设备是否连上互联网
        :return:
        """
        if 'unknown' in str(self.shell('ping -w 1 www.baidu.com').stdout.readlines()[0]):
            return False
        else:
            return True


class MyTestCase(unittest.TestCase, ADB):

    driver = u2.connect(ADB().device_id)
    package_name = 'com.verifone.scb.presentation'

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        d = self.driver
        # 清除应用用户数据
        ADB().clear_app_data(self.package_name)
        d.app_start(self.package_name)
        d(resourceId="com.verifone.scb.presentation:id/et_username").set_text("TMR0001")
        d.click(0.914, 0.957)
        d(resourceId="com.verifone.scb.presentation:id/et_passwd").set_text("0000")
        d.click(0.752, 0.954)
        time.sleep(2)


    # 有wifi有非接
    def test_1_Wife_CTLS_Sale250(self):
        warnings.simplefilter("ignore", ResourceWarning)
        d = self.driver
        # load config
        d.click(0.914, 0.073)
        d.click(0.287, 0.511)
        time.sleep(1)
        d.click(0.5, 0.855)
        d.click(0.489, 0.508)
        d.click(0.484, 0.738)
        d.click(0.51, 0.63)
        d.click(0.161, 0.514)
        d.click(0.494, 0.852)
        d.click(0.722, 0.954)
        time.sleep(8)
        # 设置wifi为开启
        d.click(0.101, 0.244)
        d.click(0.171, 0.525)
        d.click(0.474, 0.514)
        d.click(0.823, 0.514)
        d.click(0.151, 0.625)
        d.click(0.484, 0.633)
        d.click(0.803, 0.63)
        d.click(0.742, 0.957)
        d.click(0.196, 0.414)

        # 是否连网
        if not ADB().get_network_state():
            d.click(0.883, 0.176)
        d.session(self.package_name)
        # d.shell('logcat -c')
        # time.sleep(1)

        # start_battery = str(ADB().get_battery_level())
        # start_dish = str(ADB().get_disk())
        # print('交易前电池电量：' + start_battery)
        # print('交易前磁盘信息' + start_dish)
        # cvs_list = []
        # cvs_list.append(start_battery)
        # cvs_list.append(start_dish)
        cvs_list = []
        # 单个用例执行次数
        num = 1
        # print('交易开始时间:', time.time())
        # allStart = time.time()

        for i in range(num):
            list = []
            start_battery = str(ADB().get_battery_level())
            start_dish = str(ADB().get_disk())
            print('交易前电池电量：' + start_battery)
            print('交易前磁盘信息' + start_dish)
            list.append(i + 1)
            list.append(start_battery)
            list.append(start_dish)
            oneStart = time.time()
            list.append(oneStart)
            print('第', i + 1, '次交易开始时间:', time.time())
            # 点击sale
            d.click(0.20, 0.21)
            time.sleep(0.2)
            # 点击15,执行速度太快可能只点击一个数字，不影响交易
            d.click(0.18, 0.52)
            d.click(0.48, 0.62)
            d(text='Pay').click(timeout=5)
            # 跳过tip
            d(text='Pay').click(timeout=5)
            # 页面出现Please confirm amount(THB)点击银行卡
            if d(text="Please confirm amount(THB)").exists(timeout=5):
                d.click(0.26, 0.46)
            else:
                break
            d(text='Print customer copy and back to main menu').click(timeout=10)
            oneEnd = time.time()
            start_end = oneEnd - oneStart
            list.append(oneEnd)
            list.append(start_end)
            print('第', i + 1, '次交易结束时间:', oneEnd)
            print('第', i + 1, '次交易用时:', start_end)
            if d(text="TMR0001").exists(timeout=20):
                print('返回主页面从头开始')
            else:
                break


            CPURate = ADB().get_cpu(self.package_name)
            print('CPU使用率为' + str(CPURate))
            end_battery = str(ADB().get_battery_level())
            end_dish = str(ADB().get_disk())
            list.append(end_battery)
            list.append(end_dish)
            list.append(CPURate)
            cvs_list.append(list)
            print('所有交易完成电池电量：' + end_battery)
            print('所有交易完成磁盘信息' + end_dish)

        # allEnd = time.time()
        # print('所有交易用时:', allEnd - allStart, 's')

        with open('test_1_Wife_CTLS_Sale250.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('交易次序', '交易前电池电量', '交易前磁盘信息', '开始时间', '结束时间', '交易用时', '交易后电池电量', '交易后磁盘信息', 'CPU使用率'))
            for i in cvs_list:
                writer.writerow(i)
        # 手机app log
        # d.shell('logcat -d > /sdcard/logcat.txt')
        # d.pull('/sdcard/logcat.txt',
        #        'D:\logcat.txt')

    # 有wifi无非接
    def test_2_Wife_NoCTLS_Sale250(self):
        pass

    '''
    # 无wifi有非接   那怎么连后台啊
    def test_3_NoWife_CTLS_Sale250(self):
        warnings.simplefilter("ignore", ResourceWarning)
        d = self.driver
        # package_name = 'com.verifone.scb.presentation'
        # # 清除应用用户数据
        # ADB().clear_app_data(package_name)
        # d.app_start(package_name)
        # d(resourceId="com.verifone.scb.presentation:id/et_username").set_text("TMR0001")
        # d.click(0.914, 0.957)
        # d(resourceId="com.verifone.scb.presentation:id/et_passwd").set_text("0000")
        # d.click(0.752, 0.954)
        # load config
        d.click(0.914, 0.073)
        d.click(0.287, 0.511)
        time.sleep(1)
        d.click(0.5, 0.855)
        d.click(0.489, 0.508)
        d.click(0.484, 0.738)
        d.click(0.51, 0.63)
        d.click(0.161, 0.514)
        d.click(0.494, 0.852)
        d.click(0.722, 0.954)
        time.sleep(8)

        # 是否连网
        if ADB().get_network_state():
            d.click(0.883, 0.176)
        d.session(self.package_name)
        # d.shell('logcat -c')
        # time.sleep(1)
        print('电池电量：' + str(ADB().get_battery_level()))
        print('磁盘信息' + str(ADB().get_disk()))
        # 单个用例执行次数
        num = 2
        print('交易开始时间:', time.time())
        allStart = time.time()

        for i in range(num):
            oneStart = time.time()
            print('第', i + 1, '次交易开始时间:', time.time())
            # 点击sale
            d.click(0.20, 0.21)
            time.sleep(0.2)
            # 点击15
            d.click(0.18, 0.52)
            d.click(0.48, 0.62)
            d(text='Pay').click(timeout=5)
            # 跳过tip
            d(text='Pay').click(timeout=5)
            # 页面出现Please confirm amount(THB)点击银行卡
            if d(text="Please confirm amount(THB)").exists(timeout=5):
                d.click(0.26, 0.46)
            else:
                break
            d(text='Print customer copy and back to main menu').click(timeout=10)
            print('第', i + 1, '次交易结束时间:', time.time())
            oneEnd = time.time()
            print('第', i + 1, '次交易用时:', oneEnd - oneStart)
            if d(text="TMR0001").exists(timeout=20):
                print('返回主页面从头开始')
            else:
                break

        allEnd = time.time()
        print('所有交易用时:', allEnd - allStart, 's')
        CPURate = ADB().get_cpu(self.package_name)
        print('CPU使用率为' + str(CPURate))
        print('电池电量：' + str(ADB().get_battery_level()))
        print('磁盘信息' + str(ADB().get_disk()))
        # 手机app log
        # d.shell('logcat -d > /sdcard/logcat.txt')
        # d.pull('/sdcard/logcat.txt',
        #        'D:\logcat.txt')
    '''

    # 无wifi无非接
    def test_4_NoWife_NoCTLS_Sale250(self):
        pass

    # 开启app的平均启动时间，写死是20次
    # def test_5_startAPPTime(self):
    #     TotalTime = 0
    #     PackageName = 'com.test.ui.activities.nihao'
    #     for i in range(20):
    #         Time = ADB().get_app_start_total_time('com.test.ui.activities.nihao/com.test.ui.activities.MainActivity')
    #         TotalTime = TotalTime + Time
    #         ADB().quit_app(PackageName)
    #     print('开启app的平均时间为：', TotalTime / 20, '暂不适用于SCB，scb有权限设置')

    @classmethod
    def tearDownClass(cls):
        ADB().quit_app('com.verifone.scb.presentation')


if __name__ == '__main__':
    unittest.main()

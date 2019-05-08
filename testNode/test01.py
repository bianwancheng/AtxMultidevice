'''
uiautomator2使用api 原文地址：https://github.com/openatx/uiautomator2
1、 atx的将安装步骤:
    pip install --pre -U uiautomator2 # atx经常更新，所以用这个命令安装最新版手机接到电脑上之后，需要先运行一下命令 python -m
    uiautomator2 init 将需要的程序部署到手机上，以便后续的自动化（PS：每个手机初始化一次就够了）。

2、 安装ui查看器
    因为uiautomator是独占资源，所以当atx运行的时候uiautomatorviewer是不能用的，为了减少atx频繁的启停，开发人员了基于浏览器技术的
    weditor UI查看器。https://github.com/openatx/weditor
    Windows系统可以使用命令在桌面创建一个快捷方式 python -m weditor --shortcut

3、 连接设备（sn号、ip连接、ip+port）
    import uiautomator2 as u2
    d = u2.connect('e731d13')
    d = u2.connect('10.172.24.119')
    d = u2.connect('10.172.24.119:5555') 这种方式不太理解，5555代表的是什么难道是端口？？

4、 安装app（只支持URL）
    d.app_install('http://some-domain.com/some.apk')
    使用包装可以用subprocess.Popen()安装
    sub = subprocess.Popen(['adb', 'install', '-r', 'D:\pycharm\PycharmWorkSpase\AtxMultidevice\data\\apk\Tester_0.5.apk'],
                     shell=False, stdout=subprocess.PIPE)

5、 运行/关闭app
    d.app_start('包名')
    d.app_stop('包名')
    d.app_clear('包名')
    扩展：不知道怎么获取包名的可以打开一个app，doc下运行adb shell dumpsys activity activities | findstr "Run，会得到类似的
     Run #1: ActivityRecord{3a79cdb0 u0 com.hello.scb.presentation/com.hello.adc.presentation.view.activities.MainActivity t853}
     com.hello.scb.presentation 这就是包名

6、 停止所有app/停止除了此app之外的app
    d.app_stop_all()
    d.app_stop_all(excludes=‘包名’)

7、 获取app的信息
    d.app_info('包名')
    img = d.app_icon('包名')
    img.save('存储路径名')  #如果只写图像名 则会保存在当期那文件夹下

8、 push和pull
    # push文件夹
    d.push("foo.txt", "/sdcard/")

    # push并重命名
    d.push("foo.txt", "/sdcard/bar.txt")

    # push file对象
    with open("foo.txt", 'rb') as f:
        d.push(f, "/sdcard/")

    # push 并更改文件访问方式，读、写等等
    d.push("foo.sh", "/data/local/tmp/", mode=0o755)

    d.pull("/sdcard/tmp.txt", "tmp.tx

9、 shell命令其实和subprocess.Popen差不多
    d.shell(arg) # arg可以使字符串或者list

10、 session：表示应用程序的生命周期，可以启动app可以检测app 崩溃
    sess = d.session('packageName') start app
    sess.close()  close app

    附加到正在运行的应用程序(不太理解)
    sess = d.session("com.netease.cloudmusic", attach=True)

    检查是否崩溃
    sess.running() # return True or False

11、 得到基本信息
    print(d.info)  当前包名、高度、是否旋转（猜的）、宽度、屏幕是否亮、sdk版本。有一些不知道
    {'currentPackageName': 'com.test.ui.activities.nihao', 'displayHeight': 1280, 'displayRotation': 0,
    'displaySizeDpX': 360, 'displaySizeDpY': 640, 'displayWidth': 720, 'productName': 'msm8909', 'screenOn': True,
    'sdkInt': 22, 'naturalOrientation': True}

12、 得到屏幕的尺寸
    print(d.window_size())

13、 获取当前应用程序信息
    print(d.current_app())
    {'package': 'com.test.ui.activities.nihao', 'activity': 'com.test.ui.activities.MainActivity'}

14、 等待activity出现
    d.wait_activity('com.test.ui.activities.MainActivity', timeout=10)

15、 获取sn号
    print(d.serial)

16、 获取WLAN 的ip
    print(d.wlan_ip)

17、 详细的设备信息
    print(d.device_info)
    {'udid': 'e731d13-34:87:3d:2d:60:fa-X990', 'version': '5.1.1', 'serial': 'e731d13', 'brand': 'Verifone', 'model':
    'X990', 'hwaddr': '34:87:3d:2d:60:fa', 'port': 7912, 'sdk': 22, 'agentVersion': '0.5.4', 'display': {'width': 720,
     'height': 1280}, 'battery': {'acPowered': True, 'usbPowered': False, 'wirelessPowered': False, 'status': 5,
     'health': 2, 'present': True, 'level': 100, 'scale': 100, 'voltage': 4186, 'temperature': 295, 'technology': ''}, 'memory': {'total': 922248, 'around': '1 GB'}, 'cpu': {'cores': 4, 'hardware': 'Qualcomm Technologies, Inc MSM8909'}, 'owner': None, 'presenceChangedAt': '0001-01-01T00:00:00Z', 'usingBeganAt': '0001-01-01T00:00:00Z', 'product': None, 'provider': None}

18、 屏幕的亮灭
    d.screen_on()
    d.screen_off()

19、 获取屏幕的状态
    print(d.info.get('screenOn))  return True or False

20、 软硬件的按键操作
    d.press('back')
    这些目前支持：
    home                    back                  left                  right
    up                        down
    center                   menu                 search             enter
    delete ( or del)          recent (recent apps)        volume_up           
    volume_down         volume_mute           camera    power

21、 解锁屏幕（当然是没有密码的那种）
    d.unlock()

22、事件操作
    单击、滑动、拖动操作支持百分比位置值

    1、点击：
    通过text点击 d(text='你好').click(timeout=5)
    通过坐标点击  d.click(x, y)

    2、双击：
    d.double_click(x, y, duration=0.1) #两次点击默认的时间间隔是0.1s

    3、长点击：
    d.long_click(0.515, 0.84, duration=0.5)  # 默认点击时间是0.5s

    4、滑动：
    1、 从一个坐标滑动到具体坐标
    d.swipe(sx, sy, ex, ey, duration=0.5)   # 开始坐标--结束坐标(下滑注意是大坐标变成小坐标)，滑动持续时长。有时候可能看不
    到滑动的现象可以加time.sleep(2)看一下。
    例：
    subprocess.Popen(['adb',  'shell', 'am', 'start', '-n', 'com.android.settings/.Settings'])
    time.sleep(1)
    d.swipe(0.641, 0.863, 0.348, 0.232, 0.5)

    2、把一个UI元素从中心向一个方向移动固定的步长（感觉类似拖拽了）  上、下、左、右
    d(text="Settings").swipe("down", steps=20)

    3、两点手势，从开始点到结束点（不太会用可能是以前手机的截图之类的便捷操作）
    d(text="Settings").gesture((sx1, sy1), (sx2, sy2), (ex1, ey1), (ex2, ey2))

    5、拖拽：
    d.drag(sx, sy, ex, ey, duration=0.5) # 默认点击时间是0.5s
    例：  d.drag(0.621, 0.37, 0.863, 0.576, duration=0.5)

    6、从一个UI元素拖拽到另一个UI元素
    d(text="Settings").drag_to(x, y, duration=0.2)   # duration尽量小不然会移位
    d(text="Settings").drag_to(text="Clock", duration=0.2)

    7、多点之间滑动（九宫格解锁）：
    d.swipe((x0, y0), (x1, y1), (x2, y2), duration=0.2)  # 多点坐标

23、 屏幕旋转
    natural or n
    left or l
    right or r
    upsidedown or u (can not be set)

    d.set_orientation('n')  # natural
    print(d.orientation) # 打印旋转的的状态

    控制旋转
    d.freeze_rotation(False)  # True or False

24、 截图
    d.screenshot("home.jpg")  # 存储路径

25、 获取UI的结构（可以理解成html结构）
    print(d.dump_hierarchy())

26、 查看通知栏
    d.open_notification()

27、 打开快捷下拉菜单
    d.open_quick_settings()

28、 元素选择器（个人觉得用的方便的：text、className、xpath就可以了，像一些相对定位，绝对定位，儿子，兄弟等就可以用xpath）
    text, textContains, textMatches, textStartsWith
    className, classNameMatches
    description, descriptionContains, descriptionMatches, descriptionStartsWith
    checkable, checked, clickable, longClickable
    scrollable, enabled,focusable, focused, selected
    packageName, packageNameMatches
    resourceId, resourceIdMatches
    index, instance
例：
    d(text='你好').click(timeout=5)
    d(className="android.widget.ListView").click(timeout=5)
    xpath

    有时候其实会匹配一个list的对象用索引找到实例
    d(text="Add new")[0]

    获取到元素后可以进行赋值、删除操作，也可以得到元素的value值和js差不多
    d(text="Settings").get_text()  # get widget text
    d(text="Settings").set_text("My text...")  # set the text
    d(text="Settings").clear_text()  # clear the text

29、 获取元素的中心点坐标
    x, y =d(text="Settings").center()

30、 判断一个元素是否存在
    print(d(text="Settings").exists)  # True if exists, else False

31、 隐式等待，元素存在点击
    clicked = d(text='Skip').click_exists(timeout=10.0)  # return bool
    if clicked:
        继续下面的操作

32、 获取元素对象的信息
    print(d(text='Setting').info)

33、 等待元素出现和消失
    # 等待元素出现
    d(text="Settings").wait(timeout=3.0) # return bool
    # 等待元素消失
    d(text="Settings").wait_gone(timeout=1.0)

34、fling(不知道最好的解释是什么)
    # 垂直向下滚动(default)
    d(scrollable=True).fling()
    # 水平滚动
    d(scrollable=True).fling.horiz.forward()
    # 垂直向上滚动
    d(scrollable=True).fling.vert.backward()
    # 貌似是滚动固定步长
    d(scrollable=True).fling.horiz.toBeginning(max_swipes=1000)
    # 垂直滚到低
    d(scrollable=True).fling.toEnd()

35、 滚动操作
    # 垂直向下滚动(default)
    d(scrollable=True).scroll(steps=10)
    # 水平滚动
    d(scrollable=True).scroll.horiz.forward(steps=100)
    # 垂直向上滚动
    d(scrollable=True).scroll.vert.backward()
    # 貌似是滚动固定步长
    d(scrollable=True).scroll.horiz.toBeginning(steps=100, max_swipes=1000)
    # 垂直滚到低
    d(scrollable=True).scroll.toEnd()
    # 垂直向前滚动，直到出现特定的ui对象
    d(scrollable=True).scroll.to(text="Security")

36、 Watcher（类似于监听器）
    1、当条件匹配时单击target
    如果监听到程序崩溃（AUTO_FC_WHEN_ANR出现），选择点击强制关闭
    d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait").click(text="Force Close") #这里是不是写错了应该是一个
    强制关闭一个等待

    2、如果只有一个提示可以不写具体点击什么
    d.watcher("ALERT").when(text="OK").click()
    same sa
    d.watcher("ALERT").when(text="OK").click(text='OK')

    3、当条件为真时按下一个键press
    d.watcher("ALERT").when(text="OK").press('back')

    4、检查监听器是否触发
    d.watcher("watcher_name").triggered   # return Ture or False

    5、移除特定的监听器
    d.watcher("watcher_name").remove()

    6、列举所有监听器
    d.watchers # return list

    7、检查是否触发
    d.watchers.triggered
    #  true in case of any watcher triggered

    8、重置所有监听器
    d.watchers.reset()

    9、移除所有监听器
    # remove all registered watchers
    d.watchers.remove()
    # remove the named watcher, same as d.watcher("watcher_name").remove()
    d.watchers.remove("watcher_name")

    10、强制运行所有监听器
    d.watchers.run()

    11、当页面更新时运行所有观察者。通常可以用来自动点击权限确认框，或者自动安装
    d.watcher("OK").when(text="OK").click(text="OK")
    # 启用自动触发监视程序
    d.watchers.watched = True

    # 禁用自动触发监视程序
    d.watchers.watched = False

    # 获取当前触发器监视者状态
    assert d.watchers.watched == False

37、全局设置
    # 设置每次UI点击后1.5秒的延迟
    d.click_post_delay = 1.5 # default no delay

    # 设置默认元素等待超时(秒)
    d.wait_timeout = 30.0 # default 20.0

38、 输入内容(原文说有的时候输入值点击back等键的时候无响应，需要安装一个输入法具体看原文吧)
    d.sent_keys('str')

39、Toast
    1、显示toast
    d.toast.show("Hello world", 1.0) # show for 1.0s, default 1.0s

    2、获取toast
    # 5.0: 最大等待时间
    # 10.0: toast出现后的缓存时间. 默认 10.0
    # "default message": 返回的toast值. Default None
    d.toast.get_message(5.0, 10.0, "default message")

    # 一般用法
    assert "Short message" in d.toast.get_message(5.0, default="")

    # 清除toast缓存
    d.toast.reset()

40、 xpath
    # wait exists 10s
    d.xpath("//android.widget.TextView").wait(10.0) # return bool
    # find and click
    d.xpath("//*[@content-desc='分享']").click()
    # check exists
    if d.xpath("//android.widget.TextView[contains(@text, 'Se')]").exists:
        print("exists")
    # get all text-view text, attrib and center point
    for elem in d.xpath("//android.widget.TextView").all():
        print("Text:", elem.text)
        # Dictionary eg:
        # {'index': '1', 'text': '999+', 'resource-id': 'com.netease.cloudmusic:id/qb', 'package': 'com.netease.cloudmusic', 'content-desc': '', 'checkable': 'false', 'checked': 'false', 'clickable': 'false', 'enabled': 'true', 'focusable': 'false', 'focused': 'false','scrollable': 'false', 'long-clickable': 'false', 'password': 'false', 'selected': 'false', 'visible-to-user': 'true', 'bounds': '[661,1444][718,1478]'}
        print("Attrib:", elem.attrib)
        # Coordinate eg: (100, 200)
        print("Position:", elem.center())
'''
import subprocess
import time

import uiautomator2 as u2

if __name__ == '__main__':

    d = u2.connect('10.172.24.79')
    start = time.time()
    time.sleep(2)
    end = time.time()
    print(start, end)
    print(type(end-start))
    print('耗时：', end-start, 's')
    # d(className="android.widget.TextView").set_text("0.01")  # set the text
    # d(scrollable=True).scroll()
    # d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait").click(text="Force Close")
    # d(text="Settings").swipe("down", steps=20)
    # d(text="ATX").drag_to(text='SCB smartEDC', duration=0.2)
    # d.open_notification()
    # d.open_quick_settings()
    # xml = d.dump_hierarchy()
    # print(xml)

    # d.screenshot("D:\pycharm\PycharmWorkSpase\AtxMultidevice\yamlsTestCase\home.jpg")
    # d.drag(0.621, 0.37, 0.5, 0, duration=0.5)
    # d.set_orientation('n')  # or "left"
    # print(d.orientation)
    # d.freeze_rotation(False)
    # d.healthcheck()
    # d.screen_on()
    # print(d.info.get('screenOn'))
    # print(d.wlan_ip)
    # print(d.device_info)
    # sess = d.session('com.test.ui.activities.nihao')
    # d(text='测试工具').click_exists(timeout=5.0)
    # bool = d(text='Skip').click_exists(timeout=5.0)
    # print(bool)

    # d.long_click(0.515, 0.84, 0.5)  # long click 0.5s (default)
    # subprocess.Popen(['adb',  'shell', 'am', 'start', '-n', 'com.android.settings/.Settings'])
    # d(scrollable=True).scroll(steps=10)
    # d(scrollable=True).fling()
    # time.sleep(1)
    # d(scrollable=True).fling.vert.backward()
    # d(scrollable=True).fling.toEnd()
    # time.sleep(1)
    # d.swipe(0.641, 0.863, 0.348, 0.232, 0.5)
    # d.app_clear('com.test.ui.activities.nihao')
    # d.press('back')
    # d.unlock()
    # print(d.serial)
    # print(d.info)
    # print(d.window_size())
    # print(d.current_app())
    # print(d.wait_activity('com.test.ui.activities.MainActivity', timeout=10))
    # d.app_start('com.test.ui.activities.nihao')
    # d.swipe(0, 10, 1000, 10, 0.5)
    # print(sess.running())  # True or False
    # d(text="测试工具").click()
    # sub = subprocess.Popen(['adb', 'install', '-r', 'D:\pycharm\PycharmWorkSpase\AtxMultidevice\data\\apk\Tester_0.5.apk'],
    #                  shell=False, stdout=subprocess.PIPE)
    #
    # print(sub.stdout.readlines())

    # 注意这里不要再重定向到'>', 'D:\Config\log.txt',因为stdout就可以输出控制台的值
    # log = subprocess.Popen(['adb', 'logcat', '-v', 'time'], shell=False,stdout=subprocess.PIPE)
    # print(log.stdout.readlines())  #这里需要拔掉数据线才可以有log

    # time.sleep(1)
    # img = d.app_icon('com.test.ui.activities.nihao')
    # img.save('D:\pycharm\PycharmWorkSpase\AtxMultidevice\data\\apk\\asd.png')
    # d.app_clear('com.test.ui.activities.nihao')

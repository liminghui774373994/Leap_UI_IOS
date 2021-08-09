#基础配置信息，包括全局通用方法
__author__ = "liminghui-2021-05-06"

import os
from time import sleep

import pytest
from airtest.core.api import auto_setup, device, swipe, touch
from airtest.core.cv import Template
from airtest.report.report import simple_report
from poco.drivers.ios import iosPoco




class Common:

    def get_par_path(self):
        project_file_path = os.path.abspath(os.path.join(os.path.dirname("__file__")))
        return project_file_path


    def get_path(self,moudle,pic_name):
        self.moudel = moudle
        self.pic_name = pic_name

        project_file_path = Common().get_par_path()

        pic_path = os.path.join(project_file_path,'resources',self.moudel,self.pic_name)

        return pic_path
        #


    def get_up(self):
        # 获取设备的高度和宽度
        width, height = device().get_current_resolution()
        # 校准滑动的起点和终点
        start_pt = (width / 2, height * 0.5)
        end_pt = (width / 2, height * 0.1)
        swipe(start_pt,end_pt)
        sleep(1)  # 等待设备的响应

        #
        # # 滑动5次:
        # for i in range(5):
        #     swipe(start_pt, end_pt)
        #     sleep(1)  # 等待设备的响应

    def get_down(self):
        # 获取设备的高度和宽度
        width, height = device().get_current_resolution()
        # 校准滑动的起点和终点
        start_pt = (width / 2, height * 0.1)
        end_pt = (width / 2, height * 0.9)
        swipe(start_pt, end_pt)
        sleep(1)  # 等待设备的响应

    def back_app(self):
        project_file_path = Common().get_par_path()
        wechat_path = os.path.join(project_file_path, 'resources', 'base', '微信back.png')

        touch(Template(r"%s" % wechat_path))
        sleep(1)


    def report(self):
        simple_report(__file__, logfile=r"/Users/beartwo/Documents/UI自动化/Leap_UI_IOS/report/log.txt",
                      output=r"/Users/beartwo/Documents/UI自动化/Leap_UI_IOS/report/report.html")
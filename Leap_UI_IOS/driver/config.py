# -*- encoding=utf8 -*-
__author__ = "liminghui-2021-05-08"
from airtest.core.api import *



class Driver_Config():

    def get_driver(self):

        try:
            auto_setup(__file__,logdir="/Users/beartwo/Documents/UI自动化/Leap_UI_IOS/report",devices=["iOS:///127.0.0.1:8100"])



        except Exception as e:
            raise e




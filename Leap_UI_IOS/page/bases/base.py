# -*- encoding=utf8 -*-
__author__ = "liminghui-2021-05-08"
from common.settings import *


class Base:

    def __init__(self):
        # 元素定义
        self.moudle = 'base'
        self.path = Common()
        self.back = 'back.png'





    def get_back(self):
        back_path = self.path.get_path(self.moudle, self.back)
        print(back_path)
        return back_path

























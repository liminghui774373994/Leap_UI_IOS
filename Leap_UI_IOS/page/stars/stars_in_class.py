from airtest.core.api import touch, assert_equal
from airtest.core.cv import Template
from poco.drivers.ios import iosPoco

from common.settings import Common


class Stars_Class:


    def __init__(self):
        self.path = Common()
        self.poco = iosPoco()
        self.moudle = 'test_stars'
        self.back_button = '星星换课back.png'



    def get_back_buttton(self):
        back_button = self.path.get_path('base', self.back_button)

        return back_button
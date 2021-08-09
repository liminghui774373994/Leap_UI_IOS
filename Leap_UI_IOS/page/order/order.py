from airtest.core.api import touch, assert_equal
from airtest.core.cv import Template
from poco.drivers.ios import iosPoco

from common.settings import Common


class Order:


    def __init__(self):
        self.path = Common()
        self.poco = iosPoco()
        self.moudle = 'mytab'
        self.wechat_path = '微信back.png'
        self.school_order = '校区课程'
        self.order = '其他订单'
        self.all = '全部'
        self.wait_pay = '待支付'
        self.pay = '已支付'


    def get_school_order(self):
        school_order = self.school_order
        return school_order


    def get_order(self):
        order = self.order
        return order


    def get_all_order(self):
        all_order = self.all
        return all_order

    def get_wait_pay(self):
        wait_pay = self.wait_pay
        return wait_pay

    def get_pay_order(self):
        pay_order = self.wait_pay
        return pay_order













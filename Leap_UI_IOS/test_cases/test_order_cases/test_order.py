



import pytest
from airtest.core.api import assert_exists, assert_equal, stop_app, start_app

from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config
from page.mine.mytab import My_tab
from page.order.order import Order


class TestSchool_Order:


    def test_order(self,enter_mytab):

        try:
            order = My_tab().get_order()
            iosPoco()(order).click()
            iosPoco()('其他订单').click()
            iosPoco()('待支付').click()
            value = iosPoco()('没有订单哦～').attr('name')
            assert_equal(value, '没有订单哦～', "验证我的订单功能通过")




        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, '我的订单', "验证我的订单功能不通过")

        finally:

            Common().report()
            iosPoco()("btn return").click()
            iosPoco()("btn return").click()
import pytest
from airtest.core.api import assert_exists, assert_equal, stop_app, start_app

from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config
from page.mine.mytab import My_tab
from page.order.order import Order


class TestSchool_Order:

    @pytest.mark.usefixtures("enter_mytab")
    def test_school_order(self,enter_mytab):

        try:
            order = My_tab().get_order()
            iosPoco()(order).click()
            school_order = Order().get_school_order()
            iosPoco()(school_order).click()
            Common().back_app()
            value = iosPoco()(school_order).attr('name')
            assert_equal(value, '校区课程', "验证校区订单功能通过")

        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, '校区课程', "验证校区订单功能不通过")

        finally:

            Common().report()
            iosPoco()("btn return").click()
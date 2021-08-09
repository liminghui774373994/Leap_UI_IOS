import pytest
from airtest.core.api import assert_exists, assert_equal
from poco.drivers.ios import iosPoco
from common.settings import Common
from driver.config import Driver_Config
from page.mine.mytab import My_tab


class TestShop:


    def test_shop(self,enter_mytab):


        try:
            Common().get_up()
            shop = My_tab().get_shop()
            iosPoco()(shop).click()
            Common().back_app()
            value = iosPoco()(shop).attr('visible')
            assert_equal(value, True, "验证商城功能通过")

        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, True, "验证商城功能不通过")

        finally:

            Common().report()



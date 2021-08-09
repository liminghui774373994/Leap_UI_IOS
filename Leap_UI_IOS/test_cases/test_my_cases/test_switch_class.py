import pytest
from airtest.core.api import assert_exists, assert_equal
from airtest.core.cv import Template
from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config
from page.mine.mytab import My_tab


class TestSwitch_class:




    def test_switch_class(self,enter_mytab):




        try:
            switch_class = My_tab().get_switch_classes()
            iosPoco()(switch_class).click()
            Common().back_app()
            value = iosPoco()(switch_class).attr('visible')
            assert_equal(value, True, "验证调课功能通过")

        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, True, "验证调课功能不通过")


        finally:

            Common().report()





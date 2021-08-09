import pytest
from airtest.core.api import assert_exists, assert_equal
from airtest.core.cv import Template
from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config
from page.mine.mytab import My_tab


class TestContinue_class:




    def test_continue_class(self,enter_mytab):


        try:
            continue_class = My_tab().get_continue_classes()
            iosPoco()(continue_class).click()
            Common().back_app()
            value = iosPoco()(continue_class).attr('visible')
            assert_equal(value, True, "验证续报功能通过")

        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, True, "验证续报功能不通过")


        finally:

            Common().report()



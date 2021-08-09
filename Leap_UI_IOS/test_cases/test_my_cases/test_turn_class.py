import pytest
from airtest.core.api import assert_exists, assert_equal
from airtest.core.cv import Template
from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config
from page.mine.mytab import My_tab


class TestTurn_class:



    @pytest.mark.usefixtures("enter_mytab")
    def test_turn_class(self):


        try:
            turn_class = My_tab().get_turn_classes()
            iosPoco()(turn_class).click()
            Common().back_app()
            value = iosPoco()(turn_class).attr('visible')
            assert_equal(value, True, "验证转班功能通过")
        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, True, "验证转班功能不通过")


        finally:

            Common().report()



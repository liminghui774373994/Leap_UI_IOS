import pytest
from airtest.core.api import assert_exists, assert_equal
from airtest.report.report import simple_report
from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config
from page.mine.mytab import My_tab


class TestBook:




    def test_book(self,enter_mytab):

        try:
            Common().get_up()
            book = My_tab().get_book()
            iosPoco()(book).click()
            Common().back_app()
            value = iosPoco()(book).attr('visible')
            assert_equal(value, True, "验证纸质绘本功能通过")
        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, True, "验证纸质绘本功能不通过")
        finally:

            Common().report()
from time import sleep

import pytest
from airtest.core.api import assert_exists, assert_equal, touch
from airtest.core.cv import Template
from airtest.report.report import simple_report
from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config
from page.mine.mytab import My_tab
from page.stars.stars_in_class import Stars_Class


class TestStars:

    @pytest.mark.usefixtures("enter_mytab")
    def test_stars(self,enter_mytab):
        try:
            Common().get_up()
            stars = My_tab().get_stars()
            iosPoco()(stars).click()
            sleep(4)
            """返回我的tab"""
            back_button = Stars_Class().get_back_buttton()
            touch(Template(r"%s" % back_button))
            sleep(1)
            value = iosPoco()(stars).attr('visible')
            assert_equal(value, True, "验证星星换课功能通过")

        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, True, "验证星星账单功能不通过")


        finally:

            Common().report()






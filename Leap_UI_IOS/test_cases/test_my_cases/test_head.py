import pytest
from airtest.core.api import assert_exists, assert_equal
from airtest.core.cv import Template
from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config
from page.mine.mytab import My_tab


class TestHead:




    def test_head(self,enter_mytab):



        try:
            head_path = My_tab().get_head()

            assert_exists(Template(head_path), "验证头像存在通过")

        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, True, "验证头像功能不通过")

        finally:

            Common().report()



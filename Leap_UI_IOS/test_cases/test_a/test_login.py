__author__ = "liminghui-2021-05-06"

from time import sleep

import pytest
from airtest.core.api import *
from airtest.core.cv import Template
from airtest.report.report import simple_report
from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config
from page.bases.base_login import Login


class TestLogin:


    #@pytest.mark.usefixtures("enter_mytab")
    def test_login_on(self,start_leap,enter_mytab):

        # """进入我的tab"""
        # my_button = Login().get_mytab()
        # if my_button is not None:
        #     iosPoco()(my_button).click()
        #     sleep(2)

        """切换至密码登录"""
        password_to_login = Login().get_password_to_login()
        if password_to_login is not None:
            iosPoco()(password_to_login).click()


        input_phone = Login().get_input_phone()
        iosPoco()(input_phone).click()
        sleep(1)

        clear_button_path = Login().get_clear_button()
        if clear_button_path is not None:
            touch(Template(r"%s" %clear_button_path))


        phone = Login().get_phone()
        text(phone)


        input_pass = Login().get_input_pass()
        iosPoco()(input_pass).click()

        passw = Login().get_password()
        text(passw)


        """收起键盘"""
        leap_path = Login().get_close_board()
        touch(Template("%s" % leap_path))


        """勾选隐私协议"""
        privacy_agreement = Login().get_privacy_agreement()
        if privacy_agreement is not None:
            iosPoco()(privacy_agreement).click()


        """点击登录"""
        login_button = Login().get_login_button()
        if login_button is not None:
            iosPoco()(login_button).click()
            sleep(10)

        """选中学员"""
        photo_path = Login().get_student()
        if photo_path is not None:
            touch(Template("%s" % photo_path))
            sleep(10)


        """通过判断家长中心元素存在验证已经登录成功"""

        parents_center = Login().get_parents_center()
        value = iosPoco()(parents_center).attr('name')
        try:
            assert_equal(value, '家长中心', "验证登录功能通过")

        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, True, "验证登录功能不通过")

        finally:


            Common().report()











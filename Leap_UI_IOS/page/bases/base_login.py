# -*- encoding=utf8 -*-
__author__ = "liminghui-2021-05-08"
from common.settings import *


class Login:

    def __init__(self):
        # 元素定义
        self.moudle = 'login'
        self.path = Common()
        self.parents_center = '家长中心'
        self.my_button = "我的"
        self.password_to_login = "密码登录"
        self.input_phone = "TextField"
        self.input_pass = "SecureTextField"
        self.login_icon_unselected = "login icon unselected"
        self.login_button = "登录"

        self.check_input = '定位账号输入框.png'
        self.clearbutton = '清除按钮.png'
        self.leap = '励步.png'
        self.photo = '头像.png'

        self.phone = '19600002021'
        self.passw = 'a1234567'




    def get_mytab(self):
        my_button = self.my_button
        return my_button


    def get_password_to_login(self):
        password_to_login = self.password_to_login
        return password_to_login


    def get_clear_phone(self):
        clearphone_path = self.path.get_path(self.moudle, self.check_input)

        return clearphone_path


    def get_clear_button(self):

        clear_button_path = self.path.get_path(self.moudle,self.clearbutton)

        return clear_button_path


    def get_input_phone(self):
        input_pass = self.input_phone
        return input_pass


    def get_phone(self):
        phone = self.phone
        return phone


    def get_input_pass(self):
        input_pass = self.input_pass
        return input_pass


    def get_password(self):
        password = self.passw
        return password



    def get_close_board(self):
        leap_path = self.path.get_path(self.moudle, self.leap)
        return leap_path


    def get_privacy_agreement(self):
        privacy_agreement = self.login_icon_unselected
        return privacy_agreement


    def get_login_button(self):
        login_button = self.login_button
        return login_button


    def get_student(self):
        photo_path = self.path.get_path(self.moudle, self.photo)
        return photo_path


    def get_parents_center(self):
        parents_center = self.parents_center
        return parents_center




















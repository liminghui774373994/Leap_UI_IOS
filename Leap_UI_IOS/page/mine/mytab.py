# -*- encoding=utf8 -*-
__author__ = "liminghui-2021-05-08"
__description__ = '验证常规班学员我的页面展示元素'


from common.settings import Common


class My_tab:

    def __init__(self):
        self.path = Common()
        self.parents_center = '家长中心'
        self.scan = '扫一扫.png'
        self.head = '头像.png'
        self.home_school = '学习路径.png'
        self.learning_achievement = '学习成就'
        self.advertising = '广告位.png'
        self.temporary_switch_classes = '临时调课'
        self.turn_classes = '转班'
        self.continue_classes = '续报'
        self.shop = '摩励商城'
        self.order = '我的订单'
        self.stars = '星星换课'
        self.study_card = '学习卡/兑换码'
        self.book = '纸质绘本'
        self.school = '励步摩比校区'
        self.setting = '设置'
        self.service = '专属客服'
        self.book = '纸质绘本'
        self.moudle = 'mytab'
        self.wechat_path = '微信back.png'






    def get_head(self):
        head = self.path.get_path(self.moudle, self.head)
        return head

    def get_home_school(self):
        home_school = self.path.get_path(self.moudle, self.home_school)
        return home_school


    def get_scan(self):
        scan = self.path.get_path(self.moudle, self.scan)
        return scan


    def get_learning_achievement(self):
        learning = self.learning_achievement
        return learning

    def get_advertising(self):
        advertising_path = self.path.get_path(self.moudle, self.advertising)
        print(advertising_path)
        return advertising_path


    def get_switch_classes(self):
        temporary_switch_classes = self.temporary_switch_classes
        return temporary_switch_classes


    def get_turn_classes(self):
        turn_class = self.turn_classes
        return turn_class


    def get_continue_classes(self):
        continue_class = self.continue_classes
        return continue_class

    def get_stars(self):
        stars = self.stars
        return stars


    def get_shop(self):
        shop = self.shop
        return shop

    def get_order(self):
        order = self.order
        return order


    def get_book(self):
        book = self.book
        return book


    def get_study_card(self):
        study_card = self.study_card
        return study_card

    def get_school(self):
        school = self.school
        return school

    def get_setting(self):
        setting = self.setting
        return setting


























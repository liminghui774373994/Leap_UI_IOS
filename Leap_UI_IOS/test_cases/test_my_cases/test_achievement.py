from time import sleep
from airtest.core.api import assert_equal, assert_exists, touch
from airtest.core.cv import Template
from poco.drivers.ios import iosPoco

from common.settings import Common
from conftest import enter_mytab
from page.bases.base import Base
from page.mine.mytab import My_tab


class TestAdvertising:


    def test_achievement(self,enter_mytab):

        try:
            """验证学习成就入口存在"""
            achievement = My_tab().get_learning_achievement()
            iosPoco()(achievement).click()
            sleep(2)
            Common().get_up()
            Common().get_up()
            iosPoco()("parent top btn").click()
            sleep(1)

            iosPoco()('家校零距离').click()

            study_content = My_tab().get_home_school()
            assert_exists(Template((r"%s" % study_content), record_pos=(-0.345, 0.142),
                          resolution=(1080, 1920)), "学习成就功能验证通过")
            back_path = Base().get_back()
            touch(Template(r"%s" % back_path))


        except Exception:
            value = '异常捕获'
            print('process except')
            assert_equal(value, True, "验证学习内容功能不通过")



        finally:

            Common().report()





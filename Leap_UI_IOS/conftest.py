import os
import sys
from time import sleep

import pytest
from airtest.core.api import start_app, stop_app, assert_equal

from poco.drivers.ios import iosPoco

from common.settings import Common
from driver.config import Driver_Config

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))




@pytest.fixture()
def start_leap():
    # 重启励步云学习app
    #keyevent("HOME")
    driver = Driver_Config()
    driver.get_driver()
    print("------->setup_method")

    stop_app('com.firstleap.fcs')
    start_app('com.firstleap.fcs')
    sleep(10)

@pytest.fixture()
def enter_mytab():
    home_button = '首页'
    if home_button is not None:
        iosPoco()(home_button).click()

    my_button = '我的'
    if my_button is not None:
        iosPoco()(my_button).click()

    sleep(2)



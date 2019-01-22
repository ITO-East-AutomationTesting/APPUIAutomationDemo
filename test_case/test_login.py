# coding=utf-8
import unittest
from common.desired_caps import appium_desired
from businessView.loginView import LoginView
from businessView.homeView import HomeView
from common.common_fun import Common
import time


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = appium_desired()
        commonView = Common(self.driver)
        commonView.always_allow()
        time.sleep(1)
        commonView.check_cancel_button()
        commonView = Common(self.driver)
        commonView.check_skip_button()
        self.loginView = LoginView(self.driver)

    def tearDown(self):
        self.loginView.get_screenshot()
        self.driver.quit()

    #@unittest.skip("skip")
    def test_login_by_username_password(self):
        u'''Login in by correct username and password'''
        self.loginView.input_username("tangchao0602")
        self.loginView.input_password("187118tang")
        self.loginView.click_login_button()

        # self.homeView = HomeView(self.driver)
        # self.homeView.add_task_by_template_name()
        # self.homeView.update_start_and_end_time()
        # self.homeView.click_right_button()
        # self.assertEqual('听音乐放松', self.homeView.check_my_task())


if __name__ == '__main__':
    unittest.main()
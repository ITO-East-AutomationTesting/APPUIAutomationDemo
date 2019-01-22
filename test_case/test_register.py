# coding=utf-8
import unittest
from businessView.loginView import LoginView
from businessView.registerView import RegisterView
from businessView.informatonView import InformationView
from businessView.homeView import HomeView
from common.desired_caps import appium_desired
from common.common_fun import Common
import random


class Register(unittest.TestCase):

    def setUp(self):
        self.driver = appium_desired()
        common = Common(self.driver)
        common.check_cancel_button()
        common.check_skip_button()
        self.loginView = LoginView(self.driver)

    def tearDown(self):
        self.loginView.get_screenshot()
        self.driver.quit()

    #@unittest.skip("skip test")
    def test_register_by_username_password(self):
        u'''Register by username and password'''

        self.loginView.click_register_button()
        self.registerView = RegisterView(self.driver)

        user_name = 'Chao' + 'FLX' + str(random.randint(100, 500))
        self.registerView.input_username(user_name)

        user_pwd = 'ChaoT' + str(random.randint(500, 800))
        self.registerView.input_password(user_pwd)

        email = 'ChaoT' + str(random.randint(1000, 9000)) + '@163.com'
        self.registerView.input_email(email)

        self.registerView.click_register_button()
        informationView = InformationView(self.driver)

        informationView.select_time_by_text('2016')

        informationView.select_school_by_name(u'河北', u'保定学院')

        informationView.select_major_by_text(u'工学', u'计算机科学与技术', u'计算机科学与技术')

        informationView.click_go_kyb_button()

        homeView = HomeView(self.driver)

        self.assertTrue(homeView.home_view_is_loaded, "my self button not display.")

        homeView.add_task_by_template_name()
        homeView.update_start_and_end_time()
        homeView.click_right_button()


if __name__ == '__main__':
    unittest.main()
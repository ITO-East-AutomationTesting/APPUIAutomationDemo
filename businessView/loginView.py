# coding=utf-8
from baseView.baseView import BaseView
from selenium.webdriver.common.by import By
import logging
import time


class LoginView(BaseView):
    userName = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginButton = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    registerButton = (By.ID, 'login_register_text')

    def input_username(self, username):
        self.send_keys(self.userName, username)

    def input_password(self, password):
        self.send_keys(self.password, password)

    def click_login_button(self):
        self.click(self.loginButton)

    def click_register_button(self):
        self.click(self.registerButton)

    def login_action(self, username, password):
        """Login in by username and password"""
        self.check_cancel_button()
        self.check_skip_button()

        logging.info("Login Action")
        self.input_username(username)
        time.sleep(1)
        self.input_password(password)
        time.sleep(1)
        self.click()
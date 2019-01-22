# coding=utf-8
from baseView.baseView import BaseView
from selenium.webdriver.common.by import By


class RegisterView(BaseView):
    userName_text = (By.ID, 'activity_register_username_edittext')
    password_text = (By.ID, 'activity_register_password_edittext')
    email_text = (By.ID, 'activity_register_email_edittext')
    register_button = (By.ID, 'activity_register_register_btn')

    def input_username(self, username):
        self.send_keys(self.userName_text, username)

    def input_password(self, password):
        self.send_keys(self.password_text, password)

    def input_email(self, email):
        self.send_keys(self.email_text, email)

    def click_register_button(self):
        self.click(self.register_button)

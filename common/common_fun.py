# coding=utf-8

from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging


class Common(BaseView):
    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    # skipBtn = (By.XPATH, "//*[@text='跳过 > ']")
    confimBtn = (By.XPATH, "//*[@text='确认']")

    def always_allow(self):
        try:
            confirm_button = self.driver.find_element(*self.confimBtn)
        except NoSuchElementException:
            logging.info('No confirm button')
        else:
            confirm_button.click()

    def check_cancel_button(self):
        logging.info('========Check Cancel Button========')
        try:
            cancel_button = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('No cancel button')
        else:
            cancel_button.click()

    def check_skip_button(self):
        logging.info('========Check Skip Button========')
        try:
            skip_button = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('No skip button')
        else:
            skip_button.click()

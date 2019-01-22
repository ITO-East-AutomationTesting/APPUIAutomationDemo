# coding=utf-8
from baseView.baseView import BaseView
from selenium.webdriver.common.by import By


class InformationView(BaseView):
    information_time = (By.ID, 'activity_perfectinfomation_time')
    edit_school_name = (By.ID, 'perfectinfomation_edit_school_name')
    major = (By.ID, 'activity_perfectinfomation_major')
    go_button = (By.ID, 'activity_perfectinfomation_goBtn')

    def select_time_by_text(self, text):
        # 选择考试年份
        self.click(self.information_time)
        xpath = (By.XPATH, "//android.widget.TextView[@text='%s']" % text)
        self.click(xpath)

    def select_school_by_name(self, location, school):
        # 选择目标院校
        self.click(self.edit_school_name)
        location_path = (By.XPATH, "//android.widget.TextView[@text='%s']" % location)
        self.find_element_by_scroll(location_path)
        school_path = (By.XPATH, "//android.widget.TextView[@text='%s']" % school)
        self.find_element_by_scroll(school_path)

    def select_major_by_text(self, subject, group, item):
        self.click(self.major)
        subject_path = (By.XPATH, "//android.widget.TextView[@text='%s']" % subject)
        self.find_element_by_scroll(subject_path)
        group_path = (By.XPATH, "//android.widget.TextView[@text='%s']" % group)
        self.find_element_by_scroll(group_path)
        item_path = (By.XPATH, "//*[@resource-id='com.tal.kaoyan:id/major_search_item_name'][@text='%s']" % item)
        self.find_element_by_scroll(item_path)

    def click_go_kyb_button(self):
        self.click(self.go_button)
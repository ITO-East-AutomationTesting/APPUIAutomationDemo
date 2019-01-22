# coding=utf-8
from baseView.baseView import BaseView
from selenium.webdriver.common.by import By


class HomeView(BaseView):
    no_task_button = (By.ID, 'com.tal.kaoyan:id/date_task_layout')
    add_task_button = (By.ID, 'com.tal.kaoyan:id/ivAddTask')
    task_title = (By.ID, 'com.tal.kaoyan:id/home_task_title')
    more_task_template = (By.ID, 'com.tal.kaoyan:id/rlMoreTaskTemplate')

    calendar_button = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_calendar')
    myself_button = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    start_date_time = (By.ID, 'com.tal.kaoyan:id/activity_date_addtask_timestart_startdate')
    end_date_time = (By.ID, 'com.tal.kaoyan:id/activity_date_addtask_timesend_enddate')

    year_drop_down = (By.ID, 'com.tal.kaoyan:id/activity_date_addtask_selectdate_wheelyear')
    month_drop_down = (By.ID, 'com.tal.kaoyan:id/activity_date_addtask_selectdate_wheelmonth')
    day_drop_down = (By.ID, 'com.tal.kaoyan:id/activity_date_addtask_selectdate_wheelday')
    commit_button = (By.ID, 'com.tal.kaoyan:id/activity_date_addtask_selectdate_commitbtn')
    right_button = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    #right_button = (By.NAME, '确定')


    def home_view_is_loaded(self):
        loaded = self.is_display(self.myself_button)
        return loaded

    def click_calendar_button(self):
        self.click(self.calendar_button)

    def add_task_by_template_name(self):
        self.click(self.no_task_button)
        self.click(self.no_task_button)
        self.click(self.more_task_template)
        xpath = "//android.widget.TextView[@text='听音乐放松']/parent::android.widget.LinearLayout/following-sibling::android.widget.LinearLayout"
        element_xpath = (By.XPATH, xpath)
        self.find_element_by_scroll(element_xpath)

    def update_start_and_end_time(self):
        self.click(self.start_date_time)
        self.swipe_up_by_element(self.year_drop_down)
        self.swipe_down_by_element(self.month_drop_down)
        self.swipe_down_by_element(self.day_drop_down)
        self.click(self.commit_button)
        # end time
        self.click(self.end_date_time)
        self.swipe_up_by_element(self.day_drop_down)
        self.click(self.commit_button)

    def click_right_button(self):
        self.click(self.right_button)

    def check_my_task(self):
        return self.find_element(*self.task_title).text

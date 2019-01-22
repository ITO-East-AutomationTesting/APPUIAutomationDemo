# coding=utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
import time
import os


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        try:
            # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element(*loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            logging.error('Can not find element: %s' % loc[1])
            raise
        except TimeoutException:
            logging.error('Can not find element: %s' % loc[1])
            raise

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_elements(*loc))
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            # logging.warning('Can not find element: %s' % loc[1])
            logging.error('Can not find element: %s' % loc[1])
            self.get_screenshot()
            raise

    def click(self, loc):
        logging.info('Click element by %s: %s...' % (loc[0], loc[1]))
        try:
            self.find_element(*loc).click()
            time.sleep(2)
        except AttributeError:
            raise

    def clicks(self, loc, index):
        logging.info('Click element by %s: %s...' % (loc[0], loc[1]))
        try:
            self.find_elements(*loc)[index].click()
            time.sleep(2)
        except AttributeError:
            raise

    def send_keys(self, loc, text):
        try:
            logging.info('Clear input-box: %s...' % loc[1])
            self.find_element(*loc).clear()
            logging.info('Input: %s' % text)
            self.find_element(*loc).send_keys(text)
        except AttributeError:
            raise

    # def send_keys(self, loc, index, text):
    #     try:
    #         logging.info('Clear input-box: %s...' % loc[1])
    #         self.find_elements(*loc)[index].clear()
    #         time.sleep(1)
    #
    #         logging.info('Input: %s' % text)
    #         self.find_element()[index].send_keys(text)
    #         time.sleep(2)
    #     except AttributeError:
    #         raise

    def is_display(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_display())
            return True
        except:
            return False

    def get_window_size(self):
        """获取屏幕的高度和宽度"""
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        return height, width

    def swipe_up(self):
        """向上滑动屏幕"""
        height, width = self.get_window_size()
        #start_x, start_y, end_x, end_y,
        self.driver.swipe(width/2, height * 3/4, width/2, height * 1/4)

    def swipe_down(self):
        """向下滑动屏幕"""
        height, width = self.get_windowsize()
        self.driver.swipe(width/2, height * 1/4, width/2, height * 3/4)

    def swipe_left(self):
        """向左滑动屏幕"""
        height, width = self.get_windowsize()
        self.driver.swipe(width * 3/4, height/2, width * 1/4, height/2)

    def swipe_right(self):
        """向右滑动屏幕"""
        height, width = self.get_windowsize()
        self.driver.swipe(width * 1/4, height/2, width * 3/4, height/2)

    def get_screenshot(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        shot_path = os.path.join(base_dir, 'reports/screenshot')
        if not os.path.isdir(shot_path):
            os.makedirs(shot_path)
        pic_name = 'screenshot_' + time.strftime('%Y%m%d%H%M%S') + '.png'
        pic_url = os.path.join(shot_path, pic_name)
        try:
            self.driver.get_screenshot_as_file(pic_url)
            print('screenshot_name:%s' % pic_url)
        except:
            raise

    # 获取当前activity的名称
    def get_current_activity_name(self):
        activity_name = self.driver.current_activity
        print('Current activity name is: %s' % activity_name)
        return activity_name

    def find_element_by_scroll(self, loc):
        isSwipe = True
        i = 0
        while isSwipe and i < 5:
            try:
                self.driver.find_element(*loc).click()
                isSwipe = False
            except Exception as e:
                self.swipe_up()
                time.sleep(1)
                i += 1

    def click_back_key(self):
        logging.info('Click device back key...')
        self.driver.keyevent(4)
        time.sleep(1)

    def swipe_up_by_element(self, loc):
        element = self.find_element(*loc)
        start_x = element.rect['x'] + (element.rect['width'] / 2)
        start_y = element.rect['y']
        end_x = element.rect['x'] + (element.rect['width'] / 2)
        end_y = element.rect['y'] + (element.rect['height'] / 3)
        self.driver.swipe(end_x, end_y, start_x, start_y)
        time.sleep(1)

    def swipe_down_by_element(self, loc):
        element = self.find_element(*loc)
        start_x = element.rect['x'] + (element.rect['width'] / 2)
        start_y = element.rect['y']
        end_x = element.rect['x'] + (element.rect['width'] / 2)
        end_y = element.rect['y'] + (element.rect['height'] / 3)
        self.driver.swipe(start_x, start_y, end_x, end_y)
        time.sleep(1)

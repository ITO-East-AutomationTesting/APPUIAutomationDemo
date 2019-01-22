# coding=utf-8

from appium import webdriver
import yaml
import logging
import logging.config
import os


base_dir = os.path.dirname(os.path.dirname(__file__))
log_file_path = os.path.join(base_dir, 'config/log.conf')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()


def appium_desired():
    kyb_caps_path = os.path.join(base_dir, 'config/kyb_caps.yaml')
    with open(kyb_caps_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    app_path = os.path.join(base_dir, 'app', data['appname'])

    desired_caps = {
        "platformName": data['platformName'],
        "platformVersion": data['platformVersion'],
        "deviceName": data['deviceName'],
        "app": app_path,
        "appPackage": data['appPackage'],
        "appActivity": data['appActivity'],
        "noReset": data['noReset'],
        "unicodeKeyboard": data['unicodeKeyboard'],
        "resetKeyboard": data['resetKeyboard']
    }

    logging.info('Star APP')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver


if __name__ == '__main__':
    appium_desired()
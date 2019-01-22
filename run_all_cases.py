# coding=utf-8

import os
import time
import unittest

import HTMLTestRunnerCN

base_dir = os.path.dirname(os.path.realpath(__file__))
test_cases_path = os.path.join(base_dir, 'test_case')


def create_suite():
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_cases_path, pattern='test_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTest(test_case)

    return suite


now = time.strftime('%Y%m%d%H%M%S')
reportFile = "test_report_" + now + ".html"
reportFilePath = os.path.join(base_dir, 'reports', reportFile)

all_test_cases = create_suite()
fp = open(reportFilePath, 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='UI Automation Test Report', tester='Terry')

runner.run(all_test_cases)

fp.close()

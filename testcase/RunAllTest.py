#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import unittest
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from report.runner.HTMLTestRunner3 import HTMLTestRunner


def create_suite():
    suites = unittest.TestSuite()  # 测试集
    test_dir = os.path.dirname(os.getcwd()) + '/testcase/'

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='Test_*.py',
        top_level_dir=None
    )

    for test_case in discover:
        suites.addTests(test_case)
        # print(test_case)
    return suites


def report():
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.path.abspath('.')) + '/report/' + sys.argv[1] + '_result.html'
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        report_name = os.path.dirname(os.path.abspath('.')) + '/report/' + now + 'result.html'
        # report_name = os.path.dirname(os.path.abspath('.')) + '/report/' + 'result.html'
    return report_name


if __name__ == '__main__':
    test_suites = create_suite()
    fp = open(report(), 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='测试用例执行情况'
    )
    Runner.run(test_suites)
    fp.close()

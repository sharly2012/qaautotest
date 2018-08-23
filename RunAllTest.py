#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from runner.runner.HTMLTestRunner3 import HTMLTestRunner
from util.BaseUtil import BaseUtil


def create_suite():
    suites = unittest.TestSuite()  # 测试集
    test_dir = BaseUtil().get_root_path() + '/testcase/'

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='Test_*.py',
        top_level_dir=None
    )

    for test_case in discover:
        suites.addTests(test_case)
    return suites


def report():
    if len(sys.argv) > 1:
        report_name = BaseUtil().get_root_path() + '/report/' + sys.argv[1] + '_result.html'
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        report_name = BaseUtil().get_root_path() + '/report/' + now + 'result.html'
        # report_name = GlobalVar.get_root_path() + '/report/' + 'result.html'
    return report_name


def send_mail(sender, psw, receiver, smtpserver, report_file):
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自劢化测试报告"
    msg["from"] = sender
    msg["to"] = psw
    msg["date"] = time.strftime('%a, %d %b %Y %H_%M_%S %z')
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


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

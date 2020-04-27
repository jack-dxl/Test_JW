import json
import unittest
import os
import HTMLTestRunner
from selenium import webdriver
import time
from config.image import image
from loging.log import MyLogger

log = MyLogger()
logger  = log.get_log()
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       # cls.assertTrue(expr=False, msg=self.log.debug('False'))
        print("所有执行前置条件")
        logger.info("1")
        #log.close_handle()
    def setUp(self):
        print("每次执行前置")
    def tearDown(self):
        print("每次执行后置")

    def test_login_01(self):
        print("第一条")


    def test_login_02(self):
        print("第二条")

    def test_login_03(self):
        print("第三条")

    @classmethod
    def tearDownClass(cls):
        print("所有后置条件")
        #cls.browser.quit()
if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"/reprt"+"/logs"+"csbg.html")
    f = open(file_path,"wb")
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_login_01'))


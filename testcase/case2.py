#coding=utf-8
import unittest
from Business.business import Business_Staff
from selenium import webdriver
from util.excel_util import excelUtil
import ddt
import json
import time
from loging.log import Logger
import os

file_name = os.path.dirname(os.path.dirname(__file__)) + "/config/excel/Staff.xls"
ex = excelUtil(file_name)
data = ex.get_data()
i = 0

class Staff(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = Logger.get_logger()
        cls.log.info("打开浏览器，开始登录")
        driver = webdriver.Chrome()
        cls.driver = Business_Staff(driver)
    def setUp(self):
        global i
        i = i + 1
        self.log.info(data[i][0] + data[i][1] + " " + data[i][2])
        time.sleep(3)
    def tearDown(self):
        pass
    @unittest.skip("暂不执行")
    def test_Staff01(self):
        '''新增员工-成功'''
        self.driver.Staff_title() #点击员工管理
        self.driver.Staff_add_success(i,data)

    @unittest.skip("暂不执行")
    def test_Staff02(self):
        '''新增员工-成功'''
        self.driver.Department_click() #点击部门
        self.driver.Staff_add_select(i, data)
    def test_Staff03(self):
        '''新增员工-失败'''
        self.driver.Staff_title()  # 点击员工管理
        self.driver.Department_click() #点击部门
        self.assertTrue(self.driver.Staff_add_select(i, data),"断言失败")
    def test_Staff04(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_add_select(i, data))
    def test_Staff05(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_add_select(i, data))
    def test_Staff06(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_phone(i, data))
    def test_Staff07(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_phone(i, data))
    def test_Staff08(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_phone(i, data))
    def test_Staff09(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_phone(i, data))
    def test_Staff10(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_phone(i, data))
    def test_Staff11(self):
        '''新增员工-失败'''
        pass
        #self.assertTrue(self.driver.Staff_phone(i, data))
    def test_Staff12(self):
        '''新增员工-失败'''
        pass
        #self.assertTrue(self.driver.Staff_phone(i, data))
    def test_Staff13(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_Id_again(i, data))
    def test_Staff14(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_number_error(i, data))
    def test_Staff15(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_number_error(i, data))
    def test_Staff16(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_number_error(i, data))
    def test_Staff17(self):
        '''新增员工-失败'''
        self.assertTrue(self.driver.Staff_enterprise(i, data))

    @classmethod
    def tearDownClass(cls):
        pass
        #cls.browser.quit()
if __name__ == '__main__':
    unittest.main()



#coding=utf-8
import unittest
from Business.business import Business_Department
from selenium import webdriver
from util.excel_util import excelUtil
import ddt
import json
import time
from loging.log import Logger
ex = excelUtil()
data = ex.get_data()
i = 0

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = Logger.get_logger()
        cls.log.info("打开浏览器，开始登录")
        driver = webdriver.Chrome()
        cls.driver = Business_Department(driver)
    def setUp(self):
        global i
        i = i + 1
        self.log.info(data[i][0] + data[i][1] +" "+ data[i][2])
        time.sleep(3)
    def tearDown(self):
        pass
    def test_department01(self):
        '''新增部门-成功'''
        #self.log.info(self.assertTrue(False,msg="1"))
        self.assertTrue(self.driver.drpartment_New(i,data))
        #try:
        #    self.assertTrue(False)
        #except AssertionError:
        #    self.log.error('执行失败')
    def test_department02(self):
        '''新增部门-成功'''
        self.assertTrue(self.driver.drpartment_New_test(i,data))

    def test_department03(self):
        '''新增部门-失败'''
        self.assertTrue(self.driver.drpartment_add_null())

    def test_department04(self):
        '''新增部门-失败'''
        self.assertTrue(self.driver.drpartment_add_again())

    def test_department05(self):
        '''新增部门-失败'''
        self.assertTrue(self.driver.department_NO_error())

    def test_department06(self):
        '''新增部门-失败'''
        self.assertTrue(self.driver.department_NO_error2())

    def test_department07(self):
        '''新增部门-失败'''
        self.assertTrue(self.driver.department_NO_error3())

    def test_department08(self):
        '''修改部门-成功'''
        self.assertTrue(self.driver.department_modify(i,data))

    def test_department09(self):
        '''修改部门-成功'''
        self.assertTrue(self.driver.department_edit())

    def test_department10(self):
        '''修改部门-失败'''
        self.assertTrue(self.driver.department_edit_errorme(i,data))

    def test_department11(self):
        '''修改部门-失败'''
        self.assertTrue(self.driver.department_edit_error())

    def test_department12(self):
        '''修改部门-失败'''
        self.assertTrue(self.driver.department_edit_error_again())

    def test_department13(self):
        '''注销部门-成功'''
        self.assertTrue(self.driver.department_Logout_Y())

    def test_department14(self):
        '''注销部门-失败'''
        self.assertTrue(self.driver.department_Logout_error1())

    def test_department15(self):
        '''注销部门-失败'''
        self.assertTrue(self.driver.department_Logout_error2())

    def test_department16(self):
        '''批量导入-成功'''
        self.assertTrue(self.driver.department_PL_true())

    def test_department17(self):
        '''批量导入-失败'''
        self.assertTrue(self.driver.department_PL_false())

    def test_department18(self):
        '''批量导入-失败'''
        self.assertTrue(self.driver.department_PL_error())

    def test_department19(self):
        '''查询部门-成功'''
        self.assertTrue(self.driver.department_Select())

    def test_department20(self):
        '''查询部门-成功'''
        self.assertTrue(self.driver.department_Select_cs())

    def test_department21(self):
        '''查询部门-成功'''
        self.assertTrue(self.driver.department_Select_sj())





    @classmethod
    def tearDownClass(cls):
        pass
        #cls.browser.quit()
if __name__ == '__main__':
    unittest.main()

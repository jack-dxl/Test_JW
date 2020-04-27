#coding=utf-8
import unittest
import os
import HTMLTestRunner
import time
from BeautifulReport import BeautifulReport
class RunCase(unittest.TestCase):
    def test_case1(self):
        case_path = os.path.join(os.getcwd(),'testcase')
        suite = unittest.defaultTestLoader.discover(case_path,'case1.py')
        file_path = os.path.join(os.getcwd()+"/"+ time.strftime("%Y-%m-%d %H_%M_%S") +"测试报告"+".html")
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        #f = open(file_path,'wb')
        #suite1 = unittest.TextTestRunner().run(suite)
        runner = BeautifulReport(suite).report(filename='金网测试报告'+now , description='部门测试', log_path='./report')
        #runner.run(suite)
        #f.close()
if __name__ == '__main__':
    unittest.main()


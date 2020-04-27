#coding=utf-8
import ddt
import unittest
from util.excel_util import excelUtil
from loging.log import Logger
ex = excelUtil()
data = ex.get_data()
i = 1
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = Logger.get_logger()
        cls.log.info(data[i][0] + data[i][1] + " " + data[i][2])
        cls.i = data[1][2]
        print(cls.i)
        print(cls.i.split(str=",", num=2))
    def setUp(self):
        pass
    def tearDown(self):
        global i
        i = i+1
        self.log.info(data[i][0] + (data[i][1] + " " + data[i][2]))
    def test_1(self):
        pass
    def test_2(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
        #cls.browser.quit()
if __name__ == '__main__':
    unittest.main()
#coding=utf-8
from xlutils.copy import copy
import xlrd
from loging.log import Logger
import os
log =Logger.get_logger()
class excelUtil():
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = os.path.dirname(os.path.dirname(__file__)) + "/config/excel/casetext.xls"  # excel路径
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)  # 打开excel
        self.table = self.data.sheets()[index]  # 获取sheets
        self.rows = self.table.nrows  # 获取总行数

    def get_data(self):
        try:
            result = []
            for i in range(self.rows):
                col = self.table.row_values(i)  # 读取每行数据
                result.append(col)  # 存储数据
            return result
        except Exception as e:
            log.error_log('获取测试用例数据失败，原因：%s' % e)

    def write_vlue(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 6, value)
        write_data.save(self.excel_path)
if __name__ == '__main__':
    ex = excelUtil()
    #str = ex.get_data()
    #a,b= str[1][2].split('，')
    #print(a,b)
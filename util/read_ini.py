#coding=utf-8
import configparser
import os
class ReadIni():
    def __init__(self, file_name=None, node=None):
        if file_name == None:
            file_name = os.path.dirname(os.path.dirname(__file__)) + "/config/config.ini"
        if node == None:
            self.node = 'URL'
        else:
            self.node = node
        self.cf = configparser.ConfigParser()
        self.cf.read(file_name,encoding="utf-8-sig")

    #获取value值
    def get_url(self, name):
        value = self.cf.get("URL", name)  # ini文件读取操作
        return value

    def get_LOGIN(self, name):
        value = self.cf.get("LOGIN", name)  # ini文件读取操作
        return value


if __name__ == '__main__':
    read_init = ReadIni() #实例化

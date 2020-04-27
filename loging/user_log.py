#coding=utf-8
import logging
import os
import time
import threading

#控制台输出日志
#consle = logging.StreamHandler()
#logger.addHandler(consle)
#文件输出日志


class userLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        log_dir = os.path.join(os.path.dirname(__file__),"logs/") #日志文件路径
        log_file = time.strftime("%Y-%m-%d-%H_%M") + ".log"  # 日志文件名称
        log_name = log_dir+log_file
        file_handle = logging.FileHandler(os.path.join(log_dir, log_name), encoding="utf-8")   #创建1个handle，用来写入日志文件
        formtter = logging.Formatter(' - %(filename)s - %(funName)s - %(levelno)s - %(levelname)s - %(message)s ') #日志输出格式
        file_handle.setFormatter(formtter)
        self.logger.addHandler(file_handle)
        self.logger.removeHandler(file_handle)
        #file_handle.close()
    def get_log(self):
        return self.logger

 #   def close_handle(self):
 #       self.logger.removeHandler(file_handle)
 #       self.file_handle.close()

if __name__ == "__main__":
    user = userLog()
    log = user.get_log()
    log.debug('这是一个日志记录')


#class Logger:
#    log = None
#    lock = threading.Lock()  # 创建锁
#
#    @staticmethod
#    def get_logger():
#
#        if Logger.log is None:
#            Logger.lock.acquire()  # 锁定
#            try:
#                Logger.log = userLog().logger
#            finally:
#                Logger.lock.release()  # 释放
#        return Logger.log




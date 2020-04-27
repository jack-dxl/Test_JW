import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import os
import unittest
import time
from util.read_ini import ReadIni
from loging.log import Logger
class Page():
    """
    基础类，仅用于定义一些页面常规内容及方法
    后续各个页面类继承该类实现各自页面的特别内容及方法
    """
    #filename = "E://jw/config/image/image.png" #验证码路径

    def __init__(self, driver):
        self.config = ReadIni()
        self.logger = Logger.get_logger()
        self.base_url = self.config.get_url("test_url")
        self.logger.info("打开网址："+ self.config.get_url("test_url"))
        self.driver = driver
   # def target_page(self):
   #     return self.driver.current_url == self.base_url  # 判断当前打开的url与参数给的url是否一致

    def open(self):
        """打开页面"""
        url = self.base_url
        self.driver.get(url)
        self.driver.delete_all_cookies()
        f1 = open(os.path.dirname(os.path.dirname(__file__))+"\config\cookie\cookie.txt")
        cookie = json.loads(f1.read())
        f1.close()
        for c in cookie:
            if 'expiry' in c:
                del c['expiry']
            self.driver.add_cookie(c)
        self.driver.refresh()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        return self.driver.title

    def find_element(self, *loc):
        """寻找元素"""
        try:
            # 元素可见时，返回查找到的元素；
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            # print('找不到定位元素: %s' % loc[1])
            self.logger.warning('找不到定位元素: %s' % loc[1])
            return False
        except TimeoutException:
            # print('查找元素超时: %s' % loc[1])
            self.logger.warning('查找元素超时: %s' % loc[1])
        #except InvalidArgumentException:
        #    self.logger.warning('查找元素超时: %s' % loc[1])

        except ElementClickInterceptedException:
            # print('找不到定位元素: %s' % loc[1])
            self.logger.warning('拦截了元素单击: %s' % loc[1])
        except AttributeError:
            self.logger.warning('属性错误: %s' % loc[1])
        except ElementNotInteractableException:
            self.logger.warning('元素不可交互: %s' % loc[1])


    def find_elements(self, *loc):
        """寻找多个元素"""
        try:
            #WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))  #显示等待
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            # print('%s页面未找到元素', loc)
            self.logger.warning('%s页面未找到元素', loc)
        except TimeoutException:
            self.logger.warning('查找元素超时: %s' % loc[1])
        except IndexError:
            self.logger.warning('列表索引超出范围: %s' % loc[1])
        except ElementClickInterceptedException:
            self.logger.warning('拦截了元素单击: %s' % loc[1])
        except ElementNotInteractableException:
            self.logger.warning('元素不可交互: %s' % loc[1])


    def text_clear(self, *loc):
        '''清空文本'''
        self.find_element(*loc).clear()

    def get_text(self, *loc):
        """获取文本"""
        try :
            element = self.find_element(*loc)
            return element.text
        except AttributeError:
            self.logger.error("页面中未能找到元素", loc)

    def BACK_SPACE(self,*loc):
        '''退格'''
        try:
            self.find_element(*loc).send_keys(Keys.CONTROL,'a')  #退格
            self.find_element(*loc).send_keys(Keys.BACK_SPACE)
        except AttributeError:
            # print("页面中未能找到元素", loc)
            self.logger.error("页面中未能找到元素", loc)

    def send_keys(self,  value, *loc , clear_first=True):
        """ 输入文本框
        :param value: 输入的文本
        :param clear_first: 是否清空文本框
        :param click_first: 是否点击文本框"""
        try:
            if clear_first:
                self.find_element(*loc).clear()  # 清空文本框
                self.find_element(*loc).send_keys(value)  # 输入文本
                self.logger.info("输入文本"+ value)
            else:
                self.find_element(*loc).send_keys(value)  # 输入文本
                self.logger.info("输入文本"+ value)
        except AttributeError:
            # print("页面中未能找到元素", loc)
            self.logger.error("页面中未能找到元素", loc)

    def driver_refresh(self):
        '''刷新界面'''
        self.driver.refresh()

    def switch_frame(self, loc):
        """切换frame"""
        return self.driver.switch_to.frame(loc)

    def switch_default_frame(self):
        """返回默认iframe"""
        self.driver.switch_to_default_content()
        self.logger.info("返回默认iframe")

    def click(self, *loc):
        self.logger.info('点击元素 by {}'.format(loc[1]))
        try:
            self.find_element(*loc).click()
            time.sleep(1)
        except AttributeError as e:
            # print("无法点击元素: ", e)
            self.logger.error("无法点击元素: ", e)

    def wait(self, seconds):
        """隐式等待"""
        self.driver.implicitly_wait(seconds)
        # print("等待 %d 秒" % seconds)
        self.logger.info("等待 %d 秒" % seconds)

    def WebDriverWait(self, seconds):
        """隐式等待"""
        try :
            WebDriverWait(self.driver, timeout=seconds , poll_frequency=0.5, ignored_exceptions="")
            # print("等待 %d 秒" % seconds)
            self.logger.info("等待 %d 秒" % seconds)
        except NoSuchElementException:
            self.logger.warning('超时未找到: %s')

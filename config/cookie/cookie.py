import json
import time
import os
from selenium import webdriver
from config.image import image
from util.read_ini import ReadIni
class Crawler():
    def gather():
        config = ReadIni()
        driver = webdriver.Chrome()
        filename = os.path.dirname(os.path.dirname(__file__))+ "/image/image.png"
        logurl = config.get_url("sso_url")
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get(logurl)
        print(driver.get_cookies())
        driver.find_element_by_name('username').send_keys(config.get_LOGIN("username"))
        driver.find_element_by_name('password').send_keys(config.get_LOGIN("password"))
        driver.save_screenshot(filename)  # 截屏
        element = driver.find_element_by_class_name('validateCode')  # 获取验证码位置
        Verification = image.image(element, filename)  # 调用识别验证码
        driver.find_element_by_name('validateCode').send_keys(Verification)
        driver.find_element_by_xpath('//input[@value="登  录"]').click()
        time.sleep(5)
        ### 获取cookie
        cookie = driver.get_cookies()
        print(cookie)
        jsonCookies = json.dumps(cookie)
        with open('cookie.txt', 'w') as f:
            f.write(jsonCookies)
        time.sleep(3)
        driver.close()


Crawler.gather()

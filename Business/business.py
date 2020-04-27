#!/usr/bin/python
#-*- coding:UTF-8 -*-
from pagebojects.work_config_page import Page_element
from pagebojects.basepage import Page
import time
import os
from loging.log import Logger
from selenium import webdriver

time_time = int(time.time()) #时间戳

class Business_Department():
    def __init__(self,driver):
        self.Business = Page_element(driver)
        title = self.Business.open()  # 打开浏览器
        self.log = Logger.get_logger()
        if title == "企业配置中心" :
            self.log.info("登录成功")
            self.log.info("开始执行用例")
        else:
            self.log.error('登录失败')
            exit()

    def department_click(self):
        self.Business.department_click()        #点击部门管理

    def department_cance_click(self):           #关闭窗口
        self.Business.department_cancel(0)

    def drpartment_New(self,i,data):
        self.data1,self.data2 = data[i][3].split(',')
        self.Business.department_add()      #点击添加部门
        time.sleep(3)
        self.Business.department_name(self.data1)  #输入部门名称
        self.Business.department_no(time_time)  #输入序号 序号为时间戳，保持要测的部门在第一位
        self.Business.department_yes() #点击确定
        self.Business.WebDriverWait(5)
        print(self.Business.department_Div_error())
        if "成功" in self.Business.department_Div_error():
            self.Business.department_add()  # 点击添加部门
            time.sleep(3)
            self.Business.department_superior()  # 选择上级部门
            time.sleep(3)
            self.Business.department_superior_Search(self.data1)  # 输入上级部门名称
            time.sleep(5)
            self.Business.department_Superior_Search_xz(2)  # 选择上级部门
            self.Business.department_name(self.data2)  # 输入部门名称
            self.Business.department_yes()  # 点击确定
            self.Business.WebDriverWait(7)
            if "成功" in self.Business.department_Div_error():
                self.Business.wait(15)
                self.log.info("执行成功")
                return True
            else:
                self.log.info("执行失败")
                return False
        else:
            self.log.info("失败")
            return False
    def drpartment_New_test(self,i,data):
        #self.Business.refresh() #刷新
        self.Business.department_add()      #点击添加部门
        time.sleep(3)
        self.Business.department_name(data[i][3])  #输入部门名称
        self.Business.department_no(time_time+1)  #输入序号 序号为时间戳，保持要测的部门在第一位
        self.Business.department_yes() #点击确定
        self.Business.WebDriverWait(5)
        if "成功" in self.Business.department_Div_error():
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            return False

    def drpartment_add_null(self):
        time.sleep(2)
        self.Business.department_add()  # 点击添加部门
        time.sleep(3)
        self.Business.department_yes()  # 点击确定
        time.sleep(3)
        if  "请输入部门名称" in self.Business.department_name_error():
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            return False

    def drpartment_add_again(self):
        self.Business.department_name(self.data1)  # 输入部门名称(验重)
        self.Business.department_yes()  # 点击确定
        time.sleep(3)
        if "部门名称已经存在" in self.Business.department_name_error():
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            return False

    def department_NO_error(self):
        #self.Business.department_name_clear()   #清空部门名称
        #time.sleep(1)
        self.Business.department_name(time_time)  # 输入部门名称(避免重复)
        self.Business.department_no("-135465")
        time.sleep(2)
        if "只支持大于0整数" in self.Business.department_no_error():
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            return False

    def department_NO_error2(self):
        self.Business.department_NO_clear() #清空序号
        self.Business.department_no("-/*-/-*/-") #输入序号
        time.sleep(2)
        if "只支持大于0整数" in self.Business.department_no_error():
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            return False

    def department_NO_error3(self):
        self.Business.department_NO_clear() #清空序号
        self.Business.department_no("11111111111111111111111111111111111")
        self.Business.department_yes()  # 点击确定
        self.Business.WebDriverWait(7)
        if "超过最大排序值" in self.Business.department_Div_error():
            self.log.info("执行成功")
            self.department_cance_click() #关闭窗口
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_modify(self,i,data):
        time.sleep(3)
        self.Business.department_edit() #点击编辑
        time.sleep(3)
        self.Business.department_name_clear()  # 清空部门名称
        self.Business.department_name(data[i][3])  # 输入部门名称
        self.Business.department_yes()  # 点击确定
        self.Business.WebDriverWait(7)
        print(self.Business.department_Div_error())
        if "修改成功" in self.Business.department_Div_error():
            self.log.info("执行成功")
            time.sleep(3)
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_edit(self):
        self.Business.department_edit()  # 点击编辑
        self.Business.department_superior()  # 选择上级部门
        time.sleep(3)
        self.Business.department_superior_Search(self.data1)  # 输入上级部门名称
        time.sleep(3)
        self.Business.department_Superior_Search_xz(2)  # 选择上级部门
        self.Business.WebDriverWait(5)
        if "请谨慎操作" in self.Business.department_Superior_errer():
            self.Business.department_yes()  # 点击确定
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_edit_errorme(self,i,data):
        time.sleep(12)
        self.Business.department_list(0)  # 点击第一个部门
        time.sleep(5)
        self.Business.department_edit()  # 点击编辑
        self.Business.department_superior()  # 选择上级部门
        time.sleep(3)
        self.Business.department_superior_Search(data[i][3])  # 输入上级部门名称
        time.sleep(3)
        self.Business.department_Superior_Search_xz(3)  # 选择上级部门
        self.Business.department_yes()  # 点击确定
        self.Business.WebDriverWait(5)
        print(self.Business.department_Div_error())
        if "不能选择自己为上级企业" in self.Business.department_Div_error():
            self.log.info("执行成功")
            self.department_cance_click()  # 关闭窗口
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_edit_error(self):
        self.Business.department_edit()  # 点击编辑
        time.sleep(5)
        self.Business.BACK_SPACE_all() #退格清空部门
        self.Business.department_yes()  # 点击确定
        time.sleep(5)
        if  "请输入部门名称" in self.Business.department_name_error():
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            return False

    def department_edit_error_again(self):
        self.Business.department_name(self.data2)  # 输入部门名称
        self.Business.department_yes()  # 点击确定
        time.sleep(5)
        if  "部门名称已经存在" in self.Business.department_name_error():
            self.department_cance_click()  # 关闭窗口
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_Logout_Y(self):
        self.Business.department_Logout()  # 点击注销按钮
        time.sleep(3)
        self.Business.department_Logout_yes()  #确定注销
        self.Business.WebDriverWait(7)
        print(self.Business.department_Div_error())
        if "注销成功" in self.Business.department_Div_error():
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_Logout_error1(self):
        time.sleep(2)
        self.Business.department_title_click()  # 点击导航栏主企业
        time.sleep(5)
        self.Business.department_Logout()  # 点击注销按钮
        self.Business.department_Logout_yes()  # 确定注销
        self.Business.WebDriverWait(8)
        if "不允许删除" in self.Business.department_Div_error():
            self.log.info("执行成功")
            self.department_cance_click()  # 关闭窗口
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_Logout_error2(self):
        time.sleep(2)
        self.Business.department_cxbm('测试部（企业管理员）') #搜索企业管理员所在的部门
        time.sleep(3)
        self.Business.department_nO1_click()  # 点击搜索的第一个部门
        time.sleep(5)
        self.Business.department_title_edit() # 点击注销
        self.Business.department_Logout_yes()  # 确定注销
        self.Business.WebDriverWait(8)
        if "不允许删除" in self.Business.department_Div_error():
            self.log.info("执行成功")
            self.department_cance_click()  # 关闭窗口
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_PL_true(self):
        self.Business.department_PL()  #点击批量
        time.sleep(3)
        self.Business.department_Upload()  #点击上传
        time.sleep(3)
        exe = os.path.dirname(os.path.dirname(__file__))+ "/config/exe/True.exe"
        os.popen(exe)
        time.sleep(3)
        self.Business.department_Pl_click()  #点击确定
        self.Business.WebDriverWait(6)
        print(self.Business.department_PL_Error())
        if "失败0条" in self.Business.department_PL_Error():
            self.log.info("执行成功")
            self.department_cance_click()  # 关闭窗口
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_PL_false(self):
        self.Business.department_PL()  #点击批量
        time.sleep(3)
        self.Business.department_Upload()  #点击上传
        time.sleep(3)
        exe = os.path.dirname(os.path.dirname(__file__))+ "/config/exe/false.exe"
        os.popen(exe)
        print(exe)
        time.sleep(3)
        self.Business.department_Pl_click()  #点击确定
        self.Business.WebDriverWait(6)
        print(self.Business.department_PL_Error())
        if "成功0条" in self.Business.department_PL_Error():
            self.log.info("执行成功")
            self.department_cance_click()  # 关闭窗口
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_PL_error(self):
        self.Business.department_PL()  #点击批量
        time.sleep(3)
        self.Business.department_Upload()  #点击上传
        time.sleep(3)
        exe = os.path.dirname(os.path.dirname(__file__))+ "/config/exe/error.exe"
        os.popen(exe)
        print(exe)
        time.sleep(3)
        self.Business.department_Pl_click()  #点击确定
        self.Business.WebDriverWait(6)
        print(self.Business.department_PL_Error())
        if "获取数据失败" in self.Business.department_PL_Error():
            self.log.info("执行成功")
            self.department_cance_click()  # 关闭窗口
            return True
        else:
            self.log.info("执行失败")
            self.department_cance_click()  # 关闭窗口
            return False

    def department_Select(self):
        self.Business.department_Root()  #点击根路径
        time.sleep(5)
        return True

    def department_Select_cs(self):
        self.Business.department_cxbm_clear()   #清空部门
        self.Business.department_cxbm(self.data1)   #查询部门
        time.sleep(5)
        if self.data1 in self.Business.department_nO1():
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            return False

    def department_Select_sj(self):
        self.Business.department_cxbm_BACK_SPACE()   #退格
        time.sleep(5)
        if "测试" in self.Business.department_nO1():
            self.log.info("执行成功")
            return True
        else:
            self.log.info("执行失败")
            return False

class Business_Staff():
    def __init__(self, driver):
        self.Business = Page_element(driver)
        title = self.Business.open()  # 打开浏览器
        #self.Business.login()
        self.log = Logger.get_logger()
        if title == "企业配置中心":
            self.log.info("登录成功")
            self.log.info("开始执行用例")
        else:
            self.log.info("登录失败")
            print(title)
            exit()

    def Staff_title(self):
        self.Business.Staff_Title_Yggl()  #员工管理
        time.sleep(5)

    def Staff_add(self):
        self.Business.Staff_Add() #点击员工添加
        time.sleep(3)

    def Shutdown(self):
        self.Business.Staff_Cancel()  #关闭窗口（全局可用）
        time.sleep(1)

    def Department_click(self):
        self.Business.department_Expand() #展开
        time.sleep(2)
        self.Business.department_nO1_click() #选择第一个部门
        time.sleep(5)

    def Staff_add_success(self,i,data):
        name, phone, sex, id, office_phone, country, nation, rank, post, department, department_main, position, number = data[i][3].split('、')
        self.Staff_add()  # 点击员工添加
        self.Business.Staff_Name(name)  # 输入姓名
        self.Business.Staff_Phone(phone)  # 输入手机号
        self.Business.Staff_Sex()  # 选择性别
        self.Business.Staff_Id(id)  # 输入工号
        self.Business.Staff_Office_Phone(office_phone)  # 输入办公电话
        self.Business.Staff_Country()  # 选择国籍
        self.Business.Staff_Nation()  # 选择民族
        self.Business.Staff_Rank()  # 选择企业职级
        self.Business.Staff_Post()  # 选择岗位
        self.Business.Staff_Department(department)  # 选择部门
        self.Business.Staff_Department_main()  # 选择是否主职部门
        self.Business.Staff_Position(position)  # 职务
        self.Business.Staff_Number(number)  # 序号
        self.Business.Staff_Define()  # 点击确定
        if "新增成功" in self.Business.Staff_Div_Prompt():
            print(self.Business.Staff_Div_Prompt())
            return True
        else:
            exit()

    def Staff_add_select(self,i,data):
        time.sleep(3)
        name,phone,sex,department_main = data[i][3].split('、')
        if len(sex) == 0 :
            print("性别为空")
            self.Staff_add()  # 点击员工添加
            self.Business.Staff_Name(name)  # 输入姓名
            self.Business.Staff_Phone(phone)  # 输入手机号
            self.Business.Staff_Department_main()  # 选择是否主职部门
            self.Business.Staff_Define()  # 点击确定
            if self.Business.Staff_Error() != None:
                print("执行成功")
                return True
            else:
                self.log.error("执行失败")
                return False

        elif len(name) == 0:
            print("姓名为空")
            self.Business.Staff_Name_BackP() #退格
           #self.Business.Staff_Phone(phone)  # 输入手机号
            self.Business.Staff_Sex()  # 选择性别
           # self.Business.Staff_Department_main()  # 选择是否主职部门
           # self.Business.Staff_Define()  # 点击确定
            if self.Business.Staff_Error() != None:
                print("执行成功")
                return True
            else:
                self.log.error("执行失败")
                return False

        elif len(department_main) == 0:
            print("主职部门为空")
            self.Shutdown() #取消
            self.Staff_add()  #点击员工添加
            self.Business.Staff_Name(name)  # 输入姓名
            self.Business.Staff_Phone(phone)  # 输入手机号
            self.Business.Staff_Sex()  # 选择性别
            self.Business.Staff_Define()  # 点击确定
            if self.Business.Staff_Main_error() != None:
                print("执行成功")
                return True
            else:
                self.log.error("执行失败")
                return False

        else:
            self.Business.Staff_Add()  # 点击员工添加
            self.Business.Staff_Name(name)  # 输入姓名
            self.Business.Staff_Phone(phone)  # 输入手机号
            self.Business.Staff_Sex()  # 选择性别
            self.Business.Staff_Department_main()  # 选择是否主职部门
            self.Business.Staff_Define()  # 点击确定
            if "新增成功" in self.Business.Staff_Div_Prompt():
                print(self.Business.Staff_Div_Prompt())
                return True
            else:
                exit()

    def Staff_phone(self, i, data):
        time.sleep(3)
        name,phone,sex,department_main = data[i][3].split('、')
        if len(phone) == 0:
            print("手机号为空")
            self.Shutdown()  # 取消
            self.Staff_add() #添加
            self.Business.Staff_Name(name)  # 输入姓名
            self.Business.Staff_Sex()  # 选择性别
            self.Business.Staff_Department_main()  # 选择是否主职部门
            self.Business.Staff_Define()  # 点击确定
            if self.Business.Staff_Error() != None:
                print("执行成功")
                return True
            else:
                self.log.error("执行失败")
                return False
        elif len(phone) != 11 :
            print("手机号为其他")
            self.Business.Staff_Phone(phone)  # 输入手机号
            self.Business.Staff_Define()  # 点击确定
            if self.Business.Staff_Error() != None:
                print("执行成功")
                return True
            else:
                self.log.error("执行失败")
                return False
        elif int(phone[0:3]) <= 130:
            print("手机号为其他")
            self.Business.Staff_Phone(phone)  # 输入手机号
            self.Business.Staff_Define()  # 点击确定
            if self.Business.Staff_Error() != None:
                print("执行成功")
                return True
            else:
                self.log.error("执行失败")
                return False
        else:
            print("手机号重复")
            self.Business.Staff_Phone(phone)  # 输入手机号
            self.Business.Staff_Define()  # 点击确定
            if self.Business.Staff_Error() != None:
                print("执行成功")
                self.Shutdown()  # 取消
                return True
            else:
                self.log.error("执行失败")
                self.Shutdown()  # 取消
                return False

    def Staff_Mail(self):
        pass

    def Staff_Id_again(self,i,data):
        print("工号重复")
        self.Staff_add()  # 添加
        name,phone,sex,id,main = data[i][3].split('、')
        self.Business.Staff_Name(name)  # 输入姓名
        self.Business.Staff_Phone(phone)  # 输入手机号
        self.Business.Staff_Sex()  # 选择性别
        self.Business.Staff_Id(id)  # 输入工号
        self.Business.Staff_Department_main() #选择主职
        self.Business.Staff_Define()  # 点击确定
        if self.Business.Staff_Error() != None:
            print("执行成功")
            self.Shutdown()  # 取消
            return True
        else:
            self.log.error("执行失败")
            self.Shutdown()  # 取消
            return False

    def Staff_number_error(self, i, data):
        name, phone, sex, main,number = data[i][3].split('、')
        if str.isdigit(number) == False:
            print("序号只支持大于0的整数")
            self.Staff_add()  # 添加
            self.Business.Staff_Name(name)  # 输入姓名
            self.Business.Staff_Phone(phone)  # 输入手机号
            self.Business.Staff_Sex()  # 选择性别
            self.Business.Staff_Department_main()  # 选择主职
            self.Business.Staff_Number(number)
            self.Business.Staff_Define()  # 点击确定
            if self.Business.Staff_Error() != None:
                print("执行成功")
                return True
            else:
                self.log.error("执行失败")
                return False
        else:
            print("序号超过最大值")
            self.Business.Staff_Number(number)
            if self.Business.Staff_Error() != None:
                print("执行成功")
                self.Shutdown()
                return True
            else:
                self.log.error("执行失败")
                self.Shutdown()
                return False

    def Staff_enterprise(self,i,data):
        self.Staff_add()  # 添加
        name, phone, sex, main,number = data[i][3].split('、')
        self.Business.department_title_click()  # 点击导航栏主企业
        self.Staff_add()
        self.Business.Staff_Name(name)  # 输入姓名
        self.Business.Staff_Phone(phone)  # 输入手机号
        self.Business.Staff_Sex()  # 选择性别
        self.Business.Staff_Department_main()  # 选择主职
        self.Business.Staff_Define() #点击确定
        if self.Business.Staff_Div_Prompt() != None:
            print("执行成功")
            self.Shutdown()
            return True
        else:
            self.log.error("执行失败")
            self.Shutdown()
            return False



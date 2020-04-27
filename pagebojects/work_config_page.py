from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pagebojects.basepage import Page
import time

class Page_element(Page):
    """页面对象类"""
    #登录页
    username_loc = (By.NAME, "username")  # 输入用户名
    password_loc = (By.NAME, "password")  # 输入密码
    Verification_loc = (By.NAME, "Verification") # 验证码
    submit_loc = (By.CLASS_NAME, 'btn.btn-submit.btn-block')  # 登陆按钮

    def login(self):
        self.find_element(*self.username_loc).send_keys("17601207899")  # 输入用户名
        self.find_element(*self.password_loc).send_keys("A1234567890!")
        time.sleep(7)
        #self.find_element(*self.Verification_loc).send_keys(Verification)
        self.find_element(*self.submit_loc).click()  # 点击登陆按钮
    #部门管理
    department_Click = (By.CLASS_NAME,'router-link-exact-active')#点击部门管理
    department_Add = (By.CLASS_NAME, 'el-button.btn-b.el-button--primary')  # 点击部门添加
    department_pl = (By.XPATH,'//*[@id="app"]/div/section/section/main/div[2]/div/section/div/div[2]/div/button[2]') #点击批量导入
    department_upload = (By.CLASS_NAME,'el-button.el-button--primary.el-button--small')  #点击上传
    department_pl_error = (By.XPATH,'//*[@id="app"]/div/section/section/main/div[2]/div/section/div/div[4]/div/div[2]/div/form/div/div[3]/div/div/div') #错误信息
    department_pl_click = (By.XPATH,'//*[@id="app"]/div/section/section/main/div[2]/div/section/div/div[4]/div/div[2]/div/div/button[1]') #批量确定按钮
    department_Superior = (By.XPATH, '//input[@placeholder="请选择上级部门"]')
    department_Superior_Search = (By.CSS_SELECTOR, 'div.page_view>div.el-input.el-input--prefix>input')#点击查询出来列表的部门
    department_Superior_Search_Xz = (By.CLASS_NAME,'lleaf') #选择部门
    department_Name = (By.XPATH,'//input[@placeholder="请输入部门名称"]')
    department_No = (By.XPATH, '//input[@placeholder="请输入部门序号"]')
    department_Yes = (By.XPATH, '//*[@id="app"]/div/section/section/main/div[2]/div/section/div/div[4]/div/div[2]/div/div[1]/button[1]')  # 点击部门确定
    department_Cancel = (By.CLASS_NAME, 'el-dialog__close.el-icon.el-icon-close')  # 点击部门取消
    department_Cxbm = (By.XPATH,'//input[@placeholder="输入关键字进行过滤"]') #左侧列表的部门搜索框
    department_expand = (By.CSS_SELECTOR, '.el-tree-node__content') #展开部门
    department_NO1 = (By.CSS_SELECTOR,'div.el-tree-node__children>div:nth-child(1)>div') #左侧第一个部门
    department_root = (By.XPATH,'//*[@id="app"]/div/section/section/main/div[2]/div/section/div/div[1]/div/div[2]/div[1]/div[1]/li/div/span')  # 点击企业
    department_Edit = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[2]/div/button[2]/span')  # 点击部门编辑（操作）&部门注销
    department_logout = (By.XPATH, '//div[3]/table/tbody/tr[1]/td[2]/div/button[3]/span')  # 点击部门编辑（操作）&部门注销
    department_Superior_Errer = (By.XPATH,'//*[@id="app"]/div/section/section/main/div[2]/div/section/div/div[4]/div/div[2]/div/form/div/div[1]/div/div/div[2]')   #上级部门提示错误
    department_Name_Error = (By.CLASS_NAME,'el-form-item__error')   #部门名称报错
    department_ON_Error = (By.CLASS_NAME,'el-form-item__error')   #部门序号报错
    department_Div_Error = (By.CLASS_NAME,'el-message__content')  #弹窗报错
    department_List = (By.CLASS_NAME,'cell.el-tooltip')#部门列表 可点击
    department_Title = (By.CLASS_NAME,'treeTitleName')#部门导航栏
    department_Title_Edit = (By.CLASS_NAME,'editTreeBtn')#部门导航栏 注销按钮
    department_Logout_Yes = (By.XPATH, '//*[@id="app"]/div/section/section/main/div[2]/div/section/div/div[4]/div/div[2]/div/div[3]/button[1]/span')  # 点击注销确定
    department_Logout_NO = (By.XPATH, '//*[@id="app"]/div/section/section/main/div[2]/div/section/div/div[4]/div/div[2]/div/div[3]/button[2]/span')  # 点击注销取消
    #department_Click = (By.CLASS_NAME, 'router-link-exact-active')  # 点击部门管理


    def WebDriverwait(self,seconds):  #显式等待
        self.WebDriverWait(seconds)
    def refresh(self):      #刷新
        self.driver_refresh()
    def BACK_SPACE_all(self):   #退格名称
        self.find_element(*self.department_Name).send_keys(Keys.CONTROL,'a')
        self.find_element(*self.department_Name).send_keys(Keys.BACK_SPACE)
    def department_click(self):
        self.click(*self.department_Click)  #点击部门管理
    def department_add(self):
        self.click(*self.department_Add)    #点击添加部门
    def department_add_text(self):
        return self.get_text(*self.department_Add)  # 点击添加部门
    def department_superior(self):
        self.click(*self.department_Superior)   #选择上级部门
    def department_superior_Search(self,value):
        self.find_element(*self.department_Superior_Search).send_keys(value)      #搜索上级部门
    def department_Superior_errer(self):
        return self.get_text(*self.department_Superior_Errer)  #上级部门提示
    def department_Superior_Search_xz(self,number):
        self.find_elements(*self.department_Superior_Search_Xz)[number].click() #选择第一个部门
    def department_name(self,Name):
        self.find_element(*self.department_Name).send_keys(Name)        #输入部门名称
    def department_no(self,NO):
        self.find_element(*self.department_No).send_keys(NO)        #输入部门序号
    def department_yes(self):
        self.click(*self.department_Yes)     #点击确定
    def department_cancel(self,number):
        self.find_elements(*self.department_Cancel)[number].click()      #点击关闭窗口
    def department_Expand(self):
        self.click(*self.department_expand) # 展开部门
    def department_cxbm(self,value):
        self.find_element(*self.department_Cxbm).send_keys(value)  #输入，部门左侧搜索框
    def department_cxbm_clear(self):
        self.text_clear(*self.department_Cxbm)      #清空部门左侧搜索框
    def department_cxbm_BACK_SPACE(self):
        self.find_element(*self.department_Cxbm).send_keys(Keys.BACK_SPACE)  #退格
        self.find_element(*self.department_Cxbm).send_keys(Keys.BACK_SPACE)
    def department_nO1_click(self):
        self.click(*self.department_NO1)  # 点击左侧第一个部门
    def department_nO1(self):
        return self.get_text(*self.department_NO1)   #获取文字信息
    def department_edit(self):
        self.click(*self.department_Edit) #部门编辑
    def department_Logout(self):
        self.click(*self.department_logout)#部门注销
    def department_list(self,number):
        self.find_elements(*self.department_List)[number].click()  #右侧列表，点击第一个部门
    def department_title(self,number):
        return self.find_elements(*self.department_Title)[number].text  #获取导航栏一级部门文本
    def department_title_click(self):
        self.click(*self.department_Title)  #点击导航栏主企业
    def department_name_error(self):
        return self.get_text(*self.department_Name_Error)       #部门名称错误提示
    def department_name_clear(self):
        self.text_clear(*self.department_Name)  #清空部门名称
    def department_NO_clear(self):
        self.text_clear(*self.department_No)  #清空部门序号
    def department_no_error(self):
        return self.get_text(*self.department_ON_Error)  #部门序号报错
    def department_Div_error(self):
        return self.get_text(*self.department_Div_Error)    #div弹窗报错
    def department_superior_clear(self):
        self.text_clear(*self.department_Superior)      #清空上级组织名称
    def department_Logout_yes(self,):
        self.click(*self.department_Logout_Yes)  #点击确定
    def department_PL(self):
        self.click(*self.department_pl)   #点击批量
    def department_Upload(self):
        self.click(*self.department_upload)   #点击上传
    def department_Pl_click(self):
        self.click(*self.department_pl_click)  #批量确定
    def department_PL_Error(self):
        return self.get_text(*self.department_pl_error)  #批量报错信息
    def department_Root(self):
        self.click(*self.department_root) #点击根路径
    def department_title_edit(self):
        self.find_elements(*self.department_Title_Edit)[1].click()  #部门注销（导航栏）


    '''员工管理元素'''
    Staff_Title= (By.CSS_SELECTOR,'.el-submenu__title')#点击部门管理
    Staff_Title_yggl = (By.CSS_SELECTOR, 'li.el-submenu.is-opened>ul>li:nth-child(1)')  # 点击员工管理
    Staff_Title_pldr = (By.CSS_SELECTOR, 'li.el-submenu.is-opened>ul>li:nth-child(2)')  # 点击批量导入
    Staff_Title_yghf = (By.CSS_SELECTOR, 'li.el-submenu.is-opened>ul>li:nth-child(3)')  # 点击员工恢复
    Staff_add = (By.CSS_SELECTOR, 'div.el-col.el-col-24>button:nth-child(1)')  # 点击员工添加
    Staff_batch = (By.CSS_SELECTOR, 'div.el-col.el-col-24>button:nth-child(2)')  # 点击批量更新
    Staff_name = (By.CSS_SELECTOR, 'div.el-form-item__content>div:nth-child(1)>input[placeholder="请输入姓名"]') #输入姓名
    Staff_phone = (By.CSS_SELECTOR, 'div.el-form-item__content>div:nth-child(1)>input[placeholder="请输入手机号"]') #输入手机号
    Staff_sex = (By.XPATH, '//input[@placeholder="请选择性别"]')
    Staff_mail = (By.CSS_SELECTOR, 'div.el-form-item__content>div:nth-child(1)>input[placeholder="请输入邮箱"]')
    Staff_id = (By.CSS_SELECTOR, 'div.el-form-item__content>div:nth-child(1)>input[placeholder="请输入工号"]') #输入工号
    Staff_office_phone = (By.CSS_SELECTOR, 'div.el-form-item__content>div:nth-child(1)>input[placeholder="请输入办公电话"]')  #输入办公电话
    Staff_country = (By.XPATH, '//input[@placeholder="请选择国籍/地区"]')
    Staff_nation = (By.XPATH, '//input[@placeholder="请选择民族"]')
    Staff_rank = (By.XPATH, '//input[@placeholder="请选择企业内职级"]')
    Staff_post = (By.XPATH, '//input[@placeholder="请选择岗位"]') #输入岗位
    Staff_post_select = (By.XPATH, '//div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span/span') #选择岗位（第一个）
    Staff_post_search = (By.XPATH, '//input[@placeholder="请输入岗位名称"]') #搜索岗位 输入岗位名称
    Staff_post_search_click = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/button/span')  # 搜索岗位 点击搜索
    Staff_post_determine = (By.CSS_SELECTOR, 'div.el-dialog__footer:nth-child(3)>span>button') #搜索岗位确定
    Staff_add_ = (By.CSS_SELECTOR, 'button.el-button.el-button--primary.el-button--mini') #添加任职信息按钮
    Staff_department = (By.CSS_SELECTOR, 'div.block-contect.el-col.el-col-24>div>form>div:nth-child(1)>div>div>div>div>input') #所属部门
    Staff_department_text = (By.CSS_SELECTOR, '.page_view>div>input[placeholder="输入关键字进行过滤"]')  # 搜索所属部门
    Staff_department_select = (By.CSS_SELECTOR, 'div.el-tree-node__children>div>div')  # 选择第一个部门
    Staff_department_main = (By.CSS_SELECTOR, 'div.block-contect.el-col.el-col-24>div>form>div:nth-child(2)>div>div>div>div>input') # 是否主职部门
    Staff_position = (By.CSS_SELECTOR, 'div.block-contect.el-col.el-col-24>div>form>div:nth-child(3)>div>div>div>input')  #职务
    Staff_number = (By.CSS_SELECTOR, 'div.block-contect.el-col.el-col-24>div>form>div:nth-child(4)>div>div>div>input')  # 人员序号
    staff_main = (By.CSS_SELECTOR,'span.el-link--inner') #删除职位信息
    Staff_define = (By.CSS_SELECTOR, 'div.box-shadow>button:nth-child(1)') #确定
    Staff_cancel = (By.XPATH, '//div[2]/div/section/div/div[4]/div/div[1]/button/i') #取消
    Staff_sex_list = (By.XPATH, '//*[contains(@class,"el-select-dropdown__wrap el-scrollbar__wrap")]//*[contains(span,"男")]') #性别下拉框选择男
    Staff_country_list = (By.XPATH, '//*[contains(@class,"el-select-dropdown__wrap el-scrollbar__wrap")]//*[contains(span,"巴西")]')  # 国家下拉框选择第一个
    Staff_nation_list = (By.XPATH, '//*[contains(@class,"el-select-dropdown__wrap el-scrollbar__wrap")]//*[contains(span,"回族")]')  # 民族下拉框选择第一个
    Staff_rank_list = (By.XPATH, '//*[contains(@class,"el-select-dropdown__wrap el-scrollbar__wrap")]//*[contains(span,"测试集团职级")]')  # 企业职级下拉框选择第一个
    Staff_main_list = (By.CSS_SELECTOR, '[x-placement="bottom-start"]>div>div>ul>li:nth-child(1)')  # 是否主职部门下拉框选择是
    Staff_main_list2 = (By.CSS_SELECTOR, '[x-placement="bottom-start"]>div>div>ul>li:nth-child(2)')  # 是否主职部门下拉框选择否
    #    '''错误或提示元素'''
    Staff_div_prompt = (By.CSS_SELECTOR, '.el-message__content')  #div弹窗提示
    Staff_error = (By.CSS_SELECTOR, '.el-form-item__error')  # 添加或编辑员工信息错误提示
    Staff_main_errot = (By.CSS_SELECTOR,'div>span[style="position: absolute; color: red; font-size: 12px; top: 45px; left: 15px;"]') #主职错误提示
    def Staff_Error(self):
        return self.get_text(*self.Staff_error)  #添加或编辑员工信息错误提示
    def Staff_Div_Prompt(self):
        return self.get_text(*self.Staff_div_prompt)     #div弹窗提示
    def Staff_Main_error(self):
        return self.get_text(*self.Staff_main_errot) #主职错误提示
    def Staff_Title_Yggl(self):   #员工管理
        self.click(*self.Staff_Title)
        self.click(*self.Staff_Title_yggl)
        time.sleep(3)
    def Staff_Title_Pldr(self):   #批量导入
        self.click(*self.Staff_Title)
        self.click(*self.Staff_Title_yggl)
    def Staff_Title_Yghf(self):   #员工恢复
        self.click(*self.Staff_Title)
        self.click(*self.Staff_Title_yggl)
    def Staff_Add(self):
        self.click(*self.Staff_add)   #点击添加
    def Staff_Name(self,value):
        self.send_keys(value,*self.Staff_name) #输入姓名
    def Staff_Name_BackP(self):
        self.BACK_SPACE(*self.Staff_name)
    def Staff_Phone(self,value):
        self.send_keys(value,*self.Staff_phone) #输入手机号
    def Staff_Mail(self,value):
        self.find_element(*self.Staff_mail).send_keys(value) #输入邮箱
    def Staff_Sex(self):
        self.click(*self.Staff_sex) #选择性别
        self.click(*self.Staff_sex_list) #选择男
    def Staff_Id(self,value):
        self.find_element(*self.Staff_id).send_keys(value) #输入工号
    def Staff_Office_Phone(self,value):
        self.find_element(*self.Staff_office_phone).send_keys(value) #输入办公电话
    def Staff_Country(self):
        self.click(*self.Staff_country)#选择国家地区
        self.click(*self.Staff_country_list) #选择中国大陆
    def Staff_Nation(self):
        self.click(*self.Staff_nation)#选择民族
        self.click(*self.Staff_nation_list) #选择汉族
    def Staff_Rank(self):
        self.click(*self.Staff_rank)  # 选择企业职级
        self.click(*self.Staff_rank_list)  # 选择职级
    def Staff_Post(self):
        self.click(*self.Staff_post) #选择岗位
        time.sleep(3)
        self.click(*self.Staff_post_select) #选择第一个岗位
        self.click(*self.Staff_post_determine)  #确定
    def Staff_Department(self,value):
        self.click(*self.Staff_department) #点击部门
        self.find_element(*self.Staff_department_text).send_keys(value)  #搜索部门
        time.sleep(3)
        self.click(*self.Staff_department_select) #选择部门
    def Staff_Department_main(self):
        self.click(*self.Staff_department_main) #选择是否主职部门
        self.click(*self.Staff_main_list) #选择是
    def Staff_Position(self,value):
        self.find_element(*self.Staff_position).send_keys(value) #输入职务
    def Staff_Number(self,value):
        self.send_keys(value,*self.Staff_number) #输入序号
    def Staff_Define(self):
        self.click(*self.Staff_define)  #确定
    def Staff_Cancel(self):
        self.click(*self.Staff_cancel) #取消




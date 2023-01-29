import time
from action.PageAction import *
from util.ObjectMap import *
from util.KeyBoardUtil import KeyboardKeys
from util.ClipboardUtil import Clipboard
from util.WaitUtil import WaitUtil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def TestSendMailWithAttachment():
    # 创建实例
    #print("启动浏览器")
    try:
        eval('open_browser()')
        time.sleep(5)
    except Exception as err:
        raise  err
    # open_browser()
    # # 最大化窗口
    # maximize_browser()
    # print("访问126邮箱登录页面")
    # visit_url("http://mail.126.com")
    # # 暂停5秒以便邮箱登录加载完成
    # sleep(5)
    # assert_string_in_pagesource("126网易免费邮-你的专业电子邮局")
    # print("访问126邮箱登录页成功")
    #
    # # 显示等待iframe框架出现，并且切过去
    # waitFrameToBeAvailableAndSwitchToIt("xpath", "//iframe[contains(@id,'x-URS-iframe')]")
    # print("输入登录用户名")
    # input_string("xpath", "//input[@name='email']", "cxx15371705399")
    # print("输入登录密码")
    # input_string("xpath", "//input[@name='password']", "Chen199211")
    # # 单击登录按钮
    # click("id", "dologin")
    # sleep(5)
    # assert_title("网易邮箱")
    # print("登录成功")
    # # 切换至默认句柄，以规避can't access dead object异常
    # switch_to_default_content()
    # print("添加联系人...")
    # # 显示等待通讯录的链接页面元素出现
    # waitVisibilityOfElementLocated("xpath", "//div[text()='通讯录']")
    # # 单击通讯录链接
    # click("xpath", "//div[text()='通讯录']")
    # print("单击通讯录链接")
    # # 显示等待新建联系人按钮
    # waitVisibilityOfElementLocated("xpath", "//span[text()='新建联系人']")
    # # 单击新建联系人
    # click("xpath", "//span[text()='新建联系人']")
    # print("单击新建联系人按钮")
    # # 显示等待输入联系人姓名输入框出现
    # input_string("xpath", "//a[@title='编辑详细姓名']/preceding-sibling::div/input", "lily")
    # # 父元素的同级div元素的子元素input
    # # 我们通常需要靠先找到某个有id的元素，再通过层级关系定位到我们真正想要定位的元素
    # # / … 可以定位这个元素的父亲元素
    # # / 可以定位这个元素的子元素
    # # / preceding - sibling:: 可以定位这个元素的哥哥元素
    # # / following - sibling:: 可以定位这个元素的弟弟元素
    # # 如 / input[1]
    # # 表示子元素中第一个input、 / … / preceding - sibling::div[1]
    # # 表示父元素的哥哥元素中的第一个div
    # input_string("xpath", "//*[@id='iaddress_MAIL_wrap']//input", "lily@qq.com")
    # # 设置为星标联系人
    # click("xpath", "//span[text()='设为星标联系人']/preceding-sibling::span/b")
    # # 输入联系人手机号
    # input_string("xpath", "//*[@id='iaddress_TEL_wrap']//dd//input", "18262621709")
    # # 输入备注信息
    # input_string("xpath", "//textarea", "朋友")
    # # 单击确定按钮保存新联系人
    # click("xpath", "//span[text()='确 定']")
    # time.sleep(1)
    # assert_string_in_pagesource("lily@qq.com")
    # print("添加联系人成功")


if __name__ == '__main__':
    TestSendMailWithAttachment()

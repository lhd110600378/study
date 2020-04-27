from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import traceback
class Web_fuc:
    """

    封装web自动化关键字驱动

    """

    def __init__(self):

        self.driver = None




    def open_browser(self,b=''):
        '''
        打开浏览器
        :param url:标识需要打开的浏览器，默认是谷歌浏览器
                    chrome：谷歌
                    firefox: 火狐
                    ie：ie
        :return: 返回浏览器的dirver对象
        '''

        if b=='' or b == 'chrome':
            #添加配置文件，比如cookie
            op = Options()
            op.add_argument("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36")

            self.driver = webdriver.Chrome(options=op,executable_path='./')

        else:
            pass


    def get_url(self,url):
        '''
        使用driver控制浏览器访问目标地址
        :param url:访问的URL地址
        :return:是否执行官成功
        '''
        try:
            self.driver.get(url=url)

        except Exception as e:

            print(traceback.format_exc(e))

            return False

        return True


    def click(self,xpath):
        '''
        点击页面元素
        :param xpath:页面元素的xpath路径
        :return: 是否执行成功
        '''
        try:
            ele=self.driver.find_element_by_xpath(xpath=xpath)

            ele.click()

        except Exception as e:

            print(traceback.format_exc(e))

            return False

        return True


    def switch_to(self,xpath):

        '''
        切换iframe页面
        :param xpath:iframe元素在页面中的xpath定位
        :return: 是否执行成功
        '''

        try:
            ele = self.driver.find_element_by_xpath(xpath=xpath)

            self.driver.switch_to.iframe(ele)

        except Exception as e:

            print(traceback.format_exc(e))

            return False

        return True



    def send_key(self,xpath,text):

        '''
        input输入框输入信息
        :param xpath: input在页面中xpath定位
        :param text: 在输入框输入的内容
        :return: 是否执行成功
        '''

        try:
            ele=self.driver.find_element_by_xpath(xpath=xpath)

            ele.send_keys(text)

        except Exception as e:

            print(traceback.format_exc(e))

            return False

        return True


    def get_mainwindow(self):
        '''
        获取当前页面句柄
        :return: 是否获取成功
        '''
        try:
            self.mainwindows = self.driver.current_windows_handle

        except Exception as e:

            print(traceback.format_exc(e))
            return False
        return True


    def get_handle(self,title):
        '''
        获取目标页句柄
        :param title:目标页面标题名称
        :return: 是否执行成功
        '''

        try:

            for handle in self.driver.window_handles:

                self.driver.switch_to.window(handle)

                if title in self.driver.title:

                    break

        except Exception as e:

            print(traceback.format_exc(e))

            return False

        return True


    def return_current(self):
        '''
        调回至初始页面
        :return: 是否执行成功
        '''
        try:
            self.driver.switch_to.window(self.mainwindows)
        except Exception as e:
            print(traceback.format_exc(e))

            return False

        return True
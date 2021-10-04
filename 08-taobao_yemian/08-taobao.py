from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import pymongo
from lxml import etree


# 定义一个taobao类
class taobao_infos:

    # 对象初始化
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium

        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s

    # 登录淘宝
    def login(self):
        # 打开网页
        self.browser.get(self.url)

        # 等待 密码登录选项 出现
        password_login = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/div/div[1]/a[1]')))
        password_login.click()

        # # 等待 微博登录选项 出现
        # weibo_login = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-form"]/div[5]/a[1]')))
        # weibo_login.click()

        # 等待 微博账号 出现
        weibo_user = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fm-login-id"]')))
        weibo_user.send_keys(weibo_username)

        # 等待 微博密码 出现
        weibo_pwd = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fm-login-password"]')))
        weibo_pwd.send_keys(weibo_password)

        # 等待 登录按钮 出现
        submit = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-form"]/div[4]/button')))
        submit.click()

        # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[2]/a')))
        # 输出淘宝昵称
        print(taobao_name.text)

        # 等待输入框出现
        input_target = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="q"]')))
        input_target.send_keys(your_target)

        # 等待搜索按钮出现
        button_search = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button')))
        button_search.click()

    def swipe_down(self, number):
        for i in range(int(number / 0.1)):
            # 根据i的值来滑动
            if (i % 2 == 0):
                js = "var q=document.documentElement.scrollTop=" + str(200 + 400 * i)
            else:
                js = "var q=document.documentElement.scrollTop=" + str(200 * i)
            self.browser.execute_script(js)
            sleep(0.1)

        js = "var q=document.documentElement.scrollTop=100000"
        self.browser.execute_script(js)
        sleep(0.1)

    def parse_webpage(self):
        # 获取所有的句柄
        handle_all = self.browser.window_handles
        # 跳转到第二个网页
        self.browser.switch_to.window(handle_all[1])
        # 调用函数,模拟滑动页面
        swipe_number = random.randint(1, 3)
        self.swipe_down(swipe_number)
        # 获取页面的内容
        source = self.browser.page_source
        # 用xpath解析网页
        html = etree.HTML(source)
        datas = html.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]')
        for data in datas:
            # 一页48个,循环48次
            for i in range(1, 48):
                # 打印一下,查看进度
                print(i)
                img_url = data.xpath('./div[' + str(i) + ']/div[1]/div[1]/div[1]/a/img/@data-src')[0]
                price = data.xpath('./div[' + str(i) + ']/div[2]/div[1]/div[1]/strong/text()')[0]
                price = "¥" + price
                deal = data.xpath('./div[' + str(i) + ']/div[2]/div[1]/div[2]/text()')[0]
                # 把"人付款"去掉
                deal = deal.replace('人付款', '')
                title = data.xpath('./div[' + str(i) + ']/div[2]/div[2]/a/text()')
                # 把其他不用的东西去掉
                title_all = "".join(title).replace("\n", "").replace(" ", "")
                shop = data.xpath('./div[' + str(i) + ']/div[2]/div[3]/div[1]/a/span[2]/text()')[0]
                location = data.xpath('./div[' + str(i) + ']/div[2]/div[3]/div[2]/text()')[0]
                # 保存到Mongo数据库里面
                collection.insert_one({
                    "img": img_url,
                    "price": price,
                    "deal": deal,
                    "title": title_all,
                    "shop": shop,
                    "location": location
                })


if __name__ == "__main__":
    chromedriver_path = r"E:\python3.8.3\Scripts\chromedriver.exe"  # 改成你的chromedriver的完整路径地址
    weibo_username = "改成你的账号"  # 改成你的淘宝账号
    weibo_password = "改成你的密码"  # 改成你的淘宝密码
    your_target = "美食"  # 可以把美食换成其他的搜索目标

    mongo_py = pymongo.MongoClient()
    # 连接Mongo里面的taobao数据库的data列表
    collection = mongo_py['taobao']['data']
    a = taobao_infos()
    a.login()  # 登录
    a.parse_webpage()

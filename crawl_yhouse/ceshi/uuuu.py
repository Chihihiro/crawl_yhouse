# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
import re
import json
from requests import Session
from crawl_yhouse.proxy_pool import *
import random
import socket
from crawl_yhouse.user_agent import user_agent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def cookie_to_dict(cookie_info):
    cookie_dict = {}
    for each in cookie_info:
        cookie_dict[each["name"]] = each["value"]
    return cookie_dict


def change_args(x):
    y = x.replace('\n', ',')
    z = y.split(",")
    dd = ""
    for i in z:
        d = '"' + i + '"'
        e = d.replace(":", '":"')
        f = re.sub('\s', "", e)
        dd = dd + "," + f
    dic = "{" + dd[1:] + "}"
    jd = json.loads(dic)
    return jd



from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class CrawlYhouseDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self):
        display = Display(visible=0, size=(800, 600))
        display.start()
    #     self.option = ChromeOptions()
    #     self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
    #     self.prefs = {"profile.managed_default_content_settings.images": 2}
    #     self.option.add_experimental_option("prefs", self.prefs)


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider, second=0):
        hostname = socket.gethostname()
        print(hostname)

        if hostname in ('wx09', 'wx01', 'wx02', 'wx03', 'wx04', 'wx05', 'wx06', 'wx07', 'wx08'):
            pp = ProxyPool().get_proxy().get('http')[7:]
            # pp = '115.225.85.41:4539'
        else:

            pro = [
                '112.84.210.14:4560',

            ]
            pp = random.choice(pro)
        print('本次使用的代理为', pp)
        proxies = {
            'http': pp,
        }
        DR = '/usr/local/bin/chromedriver'



        try:
            self.option = ChromeOptions()
            # self.option.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
            self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
            self.prefs = {"profile.managed_default_content_settings.images": 2}
            self.option.add_experimental_option("prefs", self.prefs)
            # pp = proxies.get('http')
            self.option.add_argument("--proxy-server=http://%s" %pp)
            self.option.add_argument('--no-sandbox')
            self.option.add_argument('blink-settings=imagesEnabled=false')
            self.option.add_argument('--disable-gpu')
            # self.option.add_argument('--headless')
            # self.option.add_argument('window-size=800x600')  # 指定浏览器分辨率
            self.option.add_argument("--disable-dev-shm-usage")
            # self.option.add_argument("load-extension=C:\\Users\\xiaod\\Desktop\\Chrome_js")
            self.option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36')
            self.driver = Chrome(executable_path=DR, options=self.option)
            self.driver.set_page_load_timeout(15)
            self.wait = WebDriverWait(self.driver, 10)
            id = re.search('\d+', request.url).group()
            try:
                self.driver.get(request.url)
                print('三连击1', self.driver.get_window_position())
                print('三连击1', self.driver.get_window_size())
                print('三连击1', self.driver.get_window_rect())

                # self.driver.execute_script("""Object.defineProperty(navigator, 'webdriver', {get: () => false,});""")
            except TimeoutException:
                print('*'*30)
                print('timeout')
                print(second)
                self.driver.quit()
                if second == 0:


                    # display.stop()
                    return self.process_request(request, spider, second=1)
                else:
                    return HtmlResponse(url=request.url, body=request.url, status=202, encoding="utf-8", request=request)
                # return HtmlResponse(url=request.url, body=request.url, status=200, encoding="utf-8", request=request)
            # 获取cookies
            user1 = self.driver.execute_script('return window.navigator.userAgent;')
            print('user1是', user1)
            user2 = self.driver.execute_script('return window.outerWidth;')
            print(user2)
            user3 = self.driver.execute_script("return window.outerHeight;")
            print(user3)
            user4 = self.driver.execute_script("return window.navigator.webdriver;")
            print('是否绕过无头检测', user4)
            try:
                time.sleep(2)
                cookies_info = self.driver.get_cookies()
                print('cookies id 为：', cookies_info)
                cookies = cookie_to_dict(cookies_info)
                self.wait.until(  # 帐号输入框
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#roomSetContainer'))
                )
                data = self.driver.execute_script('return window.localStorage.roomparams;')
                print('data为', data)

            except BaseException as e:
                print(e)
                print('休息两秒第二次再请求')
                time.sleep(2)
                cookies_info = self.driver.get_cookies()
                print('cookies id 为：', cookies_info)
                cookies = cookie_to_dict(cookies_info)
                self.wait.until(  # 帐号输入框
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#roomSetContainer'))
                )
                data = self.driver.execute_script('return window.localStorage.roomparams;')
                print('data为', data)
            else:
                self.driver.quit()
                # display.stop()
            json_data = json.loads(data)
            # 设置会话
            session = Session()
            # 传入cookies
            session.cookies.update(cookies)

            header = {
                # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Referer': 'http://hotel.elong.com/%s/' %id,
                'Origin': 'http://hotel.elong.com',
                'Host': 'hotel.elong.com',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': "*/*",
                'Accept-Encoding': "gzip, deflate",
                'Accept-Language': "zh-CN,zh;q=0.9",
                'Connection': "keep-alive",
                'Content-Length': "521"}
            json_url = 'http://hotel.elong.com/ajax/tmapidetail/gethotelroomsetjvajson'
            html = session.post(json_url, headers=header, data=json_data, proxies=proxies).text
            # html = session.post(json_url, headers=header, data=json_data).text
            self.driver.quit()#这是最后一个开关
            return HtmlResponse(url=request.url, body=html, status=200, encoding="utf-8", request=request)
        except BaseException as e:
            print(e)
            print('代理有问题')
            print(request.url)
            self.driver.quit()
            # display.stop()
            # return self.process_request(request, spider)
            second += 1
            if second <= 2:#这里设置重新获取的机会默认2等于三次
                # print('再给最后一次机会')
                return self.process_request(request, spider, second=second)
            return HtmlResponse(url=request.url, body=request.url, status=201, encoding="utf-8", request=request)
            # return response
        # else:
        #     return HtmlResponse(url=request.url, body='id不准确', status=200, encoding="utf-8", request=request)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



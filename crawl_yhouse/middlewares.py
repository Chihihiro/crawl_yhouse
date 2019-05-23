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


class CrawlYhouseSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)




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


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class CrawlYhouseDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # def __init__(self):
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

            # display = Display(visible=0, size=(1024, 768))
            # display.start()
        else:
            pro = [
                '49.67.98.131:4518',

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
            pp = proxies.get('http')
            self.option.add_argument("--proxy-server=http://%s" %pp)
            self.option.add_argument('--no-sandbox')
            self.option.add_argument('blink-settings=imagesEnabled=false')
            self.option.add_argument('--disable-gpu')
            # self.option.add_argument('--headless')
            self.option.add_argument('window-size=1920x1024')  # 指定浏览器分辨率
            self.option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36')




            if hostname == 'chihiro':
                self.driver = Chrome(options=self.option)
                self.driver.set_page_load_timeout(10)
                # js1 = "Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});"
                # js2 = '''window.navigator.chrome = { runtime: {},  }; '''
                # js3 = '''Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); '''
                # js4 = '''Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3], }); '''
                # js5 = '''if (/HeadlessChrome/.pytt(window.navigator.userAgent)) {console.log("Chrome headless detected");}'''
                # self.driver.execute_script(js1)
                # self.driver.execute_script(js2)
                # self.driver.execute_script(js3)
                # self.driver.execute_script(js4)
                # self.driver.execute_script(js5)

                # self.driver.execute_script("""Object.defineProperty(navigator, 'webdriver', {get: () => false,});""")
            else:

                self.driver = Chrome(options=self.option, executable_path=DR)
                self.driver.set_page_load_timeout(10)
                # js1 = "Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});"
                # js2 = '''window.navigator.chrome = { runtime: {},  }; '''
                # js3 = '''Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); '''
                # js4 = '''Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3], }); '''
                # js5 = '''if (/HeadlessChrome/.pytt(window.navigator.userAgent)) {console.log("Chrome headless detected");}'''
                # self.driver.execute_script(js1)
                # self.driver.execute_script(js2)
                # self.driver.execute_script(js3)
                # self.driver.execute_script(js4)
                # self.driver.execute_script(js5)
                # self.driver.execute_script("""Object.defineProperty(navigator, 'webdriver', {get: () => false,});""")
            # self.driver.set_window_position(10, 10)
            # self.driver.set_window_size(945, 1020)
            # self.driver.set_window_rect(10, 10, 945, 1020)
            # self.driver.set_page_load_timeout(20)

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
                if second == 0:
                    # self.driver.execute_script("window.stop()")
                    self.driver.quit()
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
            print('是否绕过无头检测',user4)
            try:
                time.sleep(2)
                cookies_info = self.driver.get_cookies()
                print('cookies id 为：', cookies_info)
                cookies = cookie_to_dict(cookies_info)
                data = self.driver.execute_script('return window.localStorage.roomparams;')
                print('data为', data)

            except BaseException as e:
                print(e)
                print('休息两秒第二次再请求')
                time.sleep(2)
                cookies_info = self.driver.get_cookies()
                print('cookies id 为：', cookies_info)
                cookies = cookie_to_dict(cookies_info)
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
            self.driver.quit()
            # display.stop()
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



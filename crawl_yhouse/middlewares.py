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
from easyprocess import EasyProcess
from selenium.webdriver.common.by import By

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class CrawlYhouseDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self):
        if socket.gethostname() != 'chihiro':
            self.display = Display(visible=0, size=(400, 300))
            self.display.start()
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
            # pp = '49.71.62.87:4526'
        else:

            pro = [

                '49.71.62.87:4526'
            ]
            pp = random.choice(pro)
        print('本次使用的代理为', pp)
        proxies = {
            'http': pp,
        }
        DR = '/usr/local/bin/chromedriver'
        # request.meta["proxy"] = "http://"+pp



        try:
            self.option = ChromeOptions()
            # self.option.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
            self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
            self.prefs = {"profile.managed_default_content_settings.images": 2}
            self.option.add_experimental_option("prefs", self.prefs)#不加载图片

            self.option.add_argument('blink-settings=imagesEnabled=false') #不加载图片
            self.option.add_argument('--disable-gpu')
            self.option.add_argument('--no-sandbox')
            self.option.add_argument("--disable-dev-shm-usage")
            self.option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36')

            self.option.add_argument('-proxy-server=http://' + pp)
            if hostname == 'chihiro':
                self.driver = Chrome(options=self.option)
            else:
                self.driver = Chrome(executable_path=DR, options=self.option)
            self.driver.set_page_load_timeout(15)
            self.wait = WebDriverWait(self.driver, 10)
            id = re.search('\d+', request.url).group()
            try:
                self.driver.get(request.url)
            except TimeoutException as e:
                print(e)
                print('*'*30)
                print('timeout')
                print(second)
                self.driver.quit()
                if second == 0:
                    return self.process_request(request, spider, second=1)
                else:
                    return HtmlResponse(url=request.url, body=request.url, status=202, encoding="utf-8", request=request)


            try:
                # time.sleep(1)#中间不能加延迟了反扒更厉害了
                # print(cookies)
                # self.wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, '.htype_list')) #  .htype_list
                # )# 查找roomSetContainer 后立马请求

                data = self.driver.execute_script('return window.localStorage.roomparams;')
                print('data为', data)

                # user1 = self.driver.execute_script('return window.navigator.userAgent;')
                # print('user1是', user1)
                # user2 = self.driver.execute_script('return window.outerWidth;')
                # print(user2)
                # user3 = self.driver.execute_script("return window.outerHeight;")
                # print(user3)
                # user4 = self.driver.execute_script("return window.navigator.webdriver;")
                # print('是否绕过无头检测', user4)
                # ziti = self.driver.execute_script("return document.getElementsByClassName('t24 yahei').length")
                # print('字体是：', ziti)
                if data is None:
                    for i in range(30):
                        data = self.driver.execute_script('return window.localStorage.roomparams;')
                        time.sleep(0.2)
                        print('data为', data)
                        if data is not None:
                            print('多次请求尝试:', i)
                            break
                else:
                    print('data一次请求成功')
            except BaseException as e:
                print(e)
                data = None
                cookies = None

            else:
                cookies_info = self.driver.get_cookies()
                cookies = cookie_to_dict(cookies_info)
                self.driver.quit()
            # time.sleep(1)
            # document = self.driver.execute_script('return document.querySelector("#roomSetContainer")')
            # print(document.text)
            # file = open(id+".html", "w", encoding="utf-8")
            # file.write(document.text)
            # if room:
            #     print('找到房间:', request.url)
            #
            # else:
            #     print('没有房间直接跳过')
            #     return None



            # else:
            if data is None:
                print('一直没有请求到', request.url)
                second += 1
                if second <= 2:  # 这里设置重新获取的机会默认2等于三次
                    # print('再给最后一次机会')
                    return self.process_request(request, spider, second=second)

            json_data = json.loads(data)
            # 设置会话
            session = Session()
            # 传入cookies
            session.cookies.update(cookies)



            header = {
                # 'User-Agent': random.choice(user_agent),
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
            print('请求时使用的data 为：', data)
            print('cookies 为：', cookies)
            html = session.post(json_url, headers=header, data=json_data, proxies=proxies).text
            # html = session.post(json_url, headers=header, data=json_data).text
            # self.driver.quit()#这是最后一个开关
            # self.display.stop()
            return HtmlResponse(url=request.url, body=html, status=200, encoding="utf-8", request=request)
        except BaseException as e:
            print(e)
            print('代理有问题')
            print(request.url)
            self.driver.quit()
            # self.display.stop()
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







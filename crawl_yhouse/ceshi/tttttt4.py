import asyncio
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
# from crawl_yhouse.proxy_pool import *
import random
import socket
# from crawl_yhouse.user_agent import user_agent
import time,random
# from pyppeteer.launcher import launch # 控制模拟浏览器用
# from retrying import retry #设置重试次数用的


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

import socket

from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

proxies = {
            'http': '36.250.153.191:4561'
        }
def main(url):
    option = ChromeOptions()
    # self.option.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    prefs = {"profile.managed_default_content_settings.images": 2}
    option.add_experimental_option("prefs", prefs)  # 不加载图片
    option.add_argument('--no-sandbox')
    option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片
    option.add_argument('--disable-gpu')
    # self.option.add_argument('--headless')
    # self.option.add_argument('window-size=800x600')  # 指定浏览器分辨率
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36')
    # option.add_argument('--disable-gpu')
    pp = proxies.get('http')
    option.add_argument('--proxy-server=http://106.57.22.60:4565')
    # 这份目前是能够请求到的
    DR = '/usr/local/bin/chromedriver'

    hostname = socket.gethostname()
    if hostname == 'chihiro':
        driver = Chrome(options=option)
        # driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME, options=option)
    else:
        display = Display(visible=0, size=(800, 600))
        display.start()
        driver = Chrome(executable_path=DR, options=option)

    driver.set_page_load_timeout(15)
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    time.sleep(10)
    # wait.until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '.htype_list')))

    data = driver.execute_script('return window.localStorage.roomparams;')
    print('data是:', data)



    user4 = driver.execute_script("return window.navigator.webdriver;")
    print('是否绕过无头检测', user4)

    # cookies_info = driver.get_cookies()
    # print('cookies id 为：', cookies_info)
    # cookies = cookie_to_dict(cookies_info)

    # print(driver.page_source)
    # print(cookies)
    # data = driver.execute_script('return window.localStorage.roomparams;')
    # driver.quit()

    # return [data, cookies]



if __name__ == '__main__':
    url = 'http://hotel.elong.com/52001128/'
    ll = main(url)
    # request_111(ll)



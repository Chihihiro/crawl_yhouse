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

proxies = {
            'http': '182.111.157.217:4562'
        }
def main(url):
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-gpu')
    pp = '182.111.157.217:4562'
    option.add_argument('-proxy-server=http://' + pp)
    DR = '/usr/local/bin/chromedriver'
    hostname = socket.gethostname()
    if hostname == 'chihiro':
        driver = Chrome(options=option)
    else:
        display = Display(visible=1, size=(800, 600))
        display.start()
        driver = Chrome(executable_path=DR, options=option)

    driver.set_page_load_timeout(15)
    wait = WebDriverWait(driver, 10)
    driver.get(url)

    # user4 = driver.execute_script("return window.navigator.webdriver;")
    # print('是否绕过无头检测', user4)

    cookies_info = driver.get_cookies()
    # print('cookies id 为：', cookies_info)
    cookies = cookie_to_dict(cookies_info)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.htype_list'))
    )  # 查找roomSetContainer 后立马请求
    # print(driver.page_source)
    data = driver.execute_script('return window.localStorage.roomparams;')
    driver.quit()

    return [data, cookies]


def request_111(all):
    # data = """
    # {"aBTestVersion":"old","bookingChannel":1,"cardNo":192928,"checkInDate":"2019-05-23","checkOutDate":"2019-05-24","customerLevel":11,"hotelIDs":"52001128","isAfterCouponPrice":true,"isDebug":false,"isLogin":false,"isMobileOnly":false,"isNeed5Discount":false,"isTrace":false,"language":"cn","needDataFromCache":true,"needPromotion":true,"newABVersion":"Z","newVersion":false,"orderFromID":50,"payMethod":0,"productType":0,"promotionChannelCode":"0000","proxyID":"ZD","sellChannel":1,"settlementType":0,"updateOrder":false,"version":"G","elongToken":"807cfb18-c85d-4595-9792-406bafe2ff6e","code":9070882}"""
    #
    #
    # cookies = [{'name': 'SessionGuid', 'value': '21660364-1b99-4e12-bff8-b5af1e3db3f4', 'domain': '.elong.com', 'path': '/', 'expires': -1, 'size': 47, 'httpOnly': True, 'secure': False, 'session': True}, {'name': 'newjava1', 'value': '654319cf9df6af232f0bb4168a7b9e6e', 'domain': 'hotel.elong.com', 'path': '/', 'expires': -1, 'size': 40, 'httpOnly': False, 'secure': False, 'session': True}, {'name': 'CookieGuid', 'value': '807cfb18-c85d-4595-9792-406bafe2ff6e', 'domain': '.elong.com', 'path': '/', 'expires': 1621649978.365393, 'size': 46, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 's_visit', 'value': '1', 'domain': '.elong.com', 'path': '/', 'expires': 1558603143, 'size': 8, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'ShHotel', 'value': 'InDate=2019-05-23&OutDate=2019-05-24', 'domain': '.elong.com', 'path': '/', 'expires': 1561193343.023462, 'size': 43, 'httpOnly': False, 'secure': False, 'session': False}, {'name': '_fid', 'value': '807cfb18-c85d-4595-9792-406bafe2ff6e', 'domain': '.elong.com', 'path': '/', 'expires': 253402300799, 'size': 40, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'SHBrowseHotel', 'value': 'cn=52001128%2C%2C%2C%2C%2C%2C%3B&', 'domain': '.elong.com', 'path': '/', 'expires': 1561193343, 'size': 46, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'Esid', 'value': 'c1ad83ac-8127-4e6e-8e06-43a8600c869a', 'domain': '.elong.com', 'path': '/', 'expires': -1, 'size': 40, 'httpOnly': True, 'secure': False, 'session': True}, {'name': 'JSESSIONID', 'value': 'DD774B95530A62C65F63F5BFAE673911', 'domain': 'hotel.elong.com', 'path': '/', 'expires': -1, 'size': 42, 'httpOnly': True, 'secure': False, 'session': True}, {'name': 'anti_token', 'value': '14585028-1F2F-4CB8-823B-725EC9F19406', 'domain': '.elong.com', 'path': '/', 'expires': -1, 'size': 46, 'httpOnly': True, 'secure': False, 'session': True}, {'name': 'com.eLong.CommonService.OrderFromCookieInfo', 'value': 'Orderfromtype=1&Parentid=50000&Status=1&Cookiesdays=0&Coefficient=0.0&Pkid=50&Priority=8000&Isusefparam=0&Makecomefrom=0&Savecookies=0', 'domain': '.elong.com', 'path': '/', 'expires': -1, 'size': 177, 'httpOnly': False, 'secure': False, 'session': True}, {'name': 's_cc', 'value': 'true', 'domain': '.elong.com', 'path': '/', 'expires': -1, 'size': 8, 'httpOnly': False, 'secure': False, 'session': True}, {'name': 'fv', 'value': 'pcweb', 'domain': '.elong.com', 'path': '/', 'expires': -1, 'size': 7, 'httpOnly': True, 'secure': False, 'session': True}, {'name': 'ext_param', 'value': 'bns%3D4%26ct%3D3', 'domain': '.elong.com', 'path': '/', 'expires': -1, 'size': 25, 'httpOnly': False, 'secure': False, 'session': True}, {'name': 's_sq', 'value': '%5B%5BB%5D%5D', 'domain': '.elong.com', 'path': '/', 'expires': -1, 'size': 17, 'httpOnly': False, 'secure': False, 'session': True}, {'name': '__tctmc', 'value': '0.179163965', 'domain': 'hotel.elong.com', 'path': '/', 'expires': -1, 'size': 18, 'httpOnly': False, 'secure': False, 'session': True}, {'name': '__tctmd', 'value': '0.1', 'domain': 'hotel.elong.com', 'path': '/', 'expires': -1, 'size': 10, 'httpOnly': False, 'secure': False, 'session': True}]
    # print(len(cookies))
    data = all[0]
    cookies = all[1]
    json_data = json.loads(data)
    # 设置会话
    session = Session()
    # 传入cookies
    # cookies_a = cookie_to_dict(cookies)
    session.cookies.update(cookies)

    id = '52001128'
    header = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'Referer': 'http://hotel.elong.com/%s/' % id,
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
    info = json.loads(html)
    print(info['hotelTipInfo']['hotelId'])


if __name__ == '__main__':
    url = 'http://hotel.elong.com/52001128/'
    ll = main(url)
    request_111(ll)



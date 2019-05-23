# import asyncio
# from scrapy import signals
# from scrapy import signals
# from scrapy.http import HtmlResponse
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import Chrome
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.chrome.options import Options
# import re
# import json
# from requests import Session
# from crawl_yhouse.proxy_pool import *
# import random
# import socket
# from crawl_yhouse.user_agent import user_agent
# import time,random
# # from pyppeteer.launcher import launch # 控制模拟浏览器用
# # from retrying import retry #设置重试次数用的
# import pyppeteer
# import os
# os.environ['PYPPETEER_CHROMIUM_REVISION'] ='588429'
# pyppeteer.DEBUG = True
#
#
# def cookie_to_dict(cookie_info):
#     cookie_dict = {}
#     for each in cookie_info:
#         cookie_dict[each["name"]] = each["value"]
#     return cookie_dict
#
#
# def change_args(x):
#     y = x.replace('\n', ',')
#     z = y.split(",")
#     dd = ""
#     for i in z:
#         d = '"' + i + '"'
#         e = d.replace(":", '":"')
#         f = re.sub('\s', "", e)
#         dd = dd + "," + f
#     dic = "{" + dd[1:] + "}"
#     jd = json.loads(dic)
#     return jd
#
#
#
# async def main(url):# 定义main协程函数，
#     #以下使用await 可以针对耗时的操作进行挂起
#
#     browser = await pyppeteer.launch({'headless': False, 'args': ['--no-sandbox'],'userDataDir': r'E:\pypp' }) # 启动pyppeteer 属于内存中实现交互的模拟器
#     page = await browser.newPage()  # 启动个新的浏览器页面
#     await page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
#
#     await page.goto(url) # 访问登录页面
#     await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''') #以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
#     await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
#     await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
#     await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
#
#
#     data = await page.evaluate('window.localStorage.roomparams;') # 如果无法通过回车键完成点击，就调用js模拟点击登录按钮。
#     print(data)
#     time.sleep(2)
#
#     cookies_info = await page.cookies()
#
#     print(cookies_info)
#     cookies = cookie_to_dict(cookies_info)
#     # await browser.close()
#     # # loop.close()
#     return [data, cookies]
#
#
# def request_111(all):
#     data = all[0]
#     cookies = all[1]
#     json_data = json.loads(data)
#     # 设置会话
#     session = Session()
#     # 传入cookies
#     session.cookies.update(cookies)
#
#     header = {
#         # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
#         'Referer': 'http://hotel.elong.com/%s/' % id,
#         'Origin': 'http://hotel.elong.com',
#         'Host': 'hotel.elong.com',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'X-Requested-With': 'XMLHttpRequest',
#         'Accept': "*/*",
#         'Accept-Encoding': "gzip, deflate",
#         'Accept-Language': "zh-CN,zh;q=0.9",
#         'Connection': "keep-alive",
#         'Content-Length': "521"}
#     json_url = 'http://hotel.elong.com/ajax/tmapidetail/gethotelroomsetjvajson'
#     html = session.post(json_url, headers=header, data=json_data).text
#     info = json.loads(html)
#     print(info['hotelTipInfo']['hotelId'])
#
#
# if __name__ == '__main__':
#     url = 'http://hotel.elong.com/52001128/'
#     loop = asyncio.get_event_loop()
#     task = asyncio.ensure_future(main(url))
#     loop.run_until_complete(task)
#     # print(task.result())
#     request_111(task.result())
#

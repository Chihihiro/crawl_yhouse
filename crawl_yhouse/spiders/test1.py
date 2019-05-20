#
# from random import choice
# from scrapy import signals
# from scrapy.http import HtmlResponse
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.common.exceptions import TimeoutException, NoAlertPresentException, UnexpectedAlertPresentException, ElementNotVisibleException
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import Chrome
# from selenium.webdriver import ChromeOptions
# import json
#
# proxies = {
#     'http': '36.57.90.65:4527',
# }
#
#
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# # option.add_argument('--headless')
# prefs = {"profile.managed_default_content_settings.images": 2}
# option.add_experimental_option("prefs", prefs)
# option.add_argument(f"--proxy-server=http://{proxies.get('http')}")
# driver = Chrome(options=option)
# import re
# url = 'http://hotel.elong.com/93468793/'
# id = re.search('\d+', url).group()
# driver.get(url)
# sleep(4)
#
# cookies_info = driver.get_cookies()
# print(cookies_info)
#
#
# def cookie_to_dict(cookie_info):
#     cookie_dict = {}
#     for each in cookie_info:
#         cookie_dict[each["name"]] = each["value"]
#     return cookie_dict
#
# cookies = cookie_to_dict(cookies_info)
#
# # html = driver.page_source
#
# data = driver.execute_script('return window.localStorage.roomparams;')
# print(data)
#
# #
# # code = driver.execute_script("""return amafunction();
# #         function amafunction() {
# #             try {
# #                 var aaa = 6823095;
# #                 var bbb = 129;
# #                 var ccc = 970;
# #                 var ddd = 738;
# #                 var fff = 789;
# #                 var eee = bbb + ddd;
# #                 var ggg = 123;
# #                 if (validatePageData()) {
# #                     return aaa
# #                 }
# #                 if (validateHeightAndWidth()) {
# #                     return aaa + eee
# #                 }
# #                 if (!validateErrorStack()) {
# #                     return aaa - ccc - fff - ggg
# #                 } else {
# #                     return aaa + ddd
# #                 }
# #             } catch(e) {
# #                 return - 99
# #             }
# #         }
# #         function validatePageData() {
# #             var temp = document.getElementsByClassName('t24 yahei');
# #             if (temp.length == 0) {
# #                 return true
# #             }
# #             return false
# #         }
# #         function validateHeightAndWidth() {
# #             var heigh = window.outerHeight;
# #             var width = window.outerWidt;
# #             if (0 == heigh || 0 == width) {
# #                 return true
# #             } else {
# #                 return false
# #             }
# #         }
# #         function validateErrorStack() {
# #             var stackDetectionKeys = ["phantomjs", "callFunction", "pyppeteer", "moz"];
# #             try {
# #                 null[0]()
# #             } catch(e) {
# #                 for (var i = 0,
# #                 len = stackDetectionKeys.length; i < len; i++) {
# #                     var stackDetectionKeyValue = stackDetectionKeys[i];
# #                     if (e.stack.indexOf(stackDetectionKeyValue) > -1) {
# #                         return true
# #                     }
# #                 }
# #             }
# #             return false
# #         };""")
# #
# # print(code)
#
#
# json_data = json.loads(data)
#
#
#
#
#
#
#
# from requests import Session
# session = Session()
# session.cookies.update(cookies)
# from crawl_yhouse.user_agent import list_header
#
# header = {
#     'User-Agent': list_header,
#     'Referer': f'http://hotel.elong.com/{id}/',
#     'Origin': 'http://hotel.elong.com',
#     'Host': 'hotel.elong.com',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Accept': "*/*",
#     'Accept-Encoding': "gzip, deflate",
#     'Accept-Language': "zh-CN,zh;q=0.9",
#     'Connection': "keep-alive",
#     'Content-Length': "521"}
#
# print(header)
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
# json_url = 'http://hotel.elong.com/ajax/tmapidetail/gethotelroomsetjvajson'
#
# info = json.loads(session.post(json_url, headers=header, data=json_data, proxies=proxies).text)
# print('houst_id:', id)
# driver.quit()
# for i in range(10):
#     print(info['hotelTipInfo']['productsInfo'][i]['priceOfDays'][0]['price'])
#
# print(info['hotelTipInfo']['hotelId'])

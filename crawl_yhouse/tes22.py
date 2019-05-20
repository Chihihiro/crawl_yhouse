#
# #     'http': http_proxy[7:],
# # }
# # print(http_proxy)
# # print(proxies)
#
# proxies = {
#     'http': '123.186.228.83:4521',
# }
#
#
#
# from requests import Session
#
# session = Session()
#
# session
#
# cookies_info = self.driver.get_cookies()
# # print(cookies_info)
# cookies = cookie_to_dict(cookies_info)
# data = self.driver.execute_script('return window.localStorage.roomparams;')
# # print(data)
# json_data = json.loads(data)
# # 设置会话
# session = Session()
# # 传入cookies
# session.cookies.update(cookies)
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
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
# json_url = 'http://hotel.elong.com/ajax/tmapidetail/gethotelroomsetjvajson'
# html = session.post(json_url, headers=header, data=json_data, proxies=proxies).text
# # info = json.loads(html)
# # print(info)
# # print('houst_id:', id)
# self.driver.quit()
# # print(info['hotelTipInfo']['productsInfo'][0]['priceOfDays'][0]['price'])
# # print(info['hotelTipInfo']['hotelId'])
# # if id == info['hotelTipInfo']['hotelId']:
# return HtmlResponse(url=request.url, body=html, status=200, encoding="utf-8", request=request)
# # else:
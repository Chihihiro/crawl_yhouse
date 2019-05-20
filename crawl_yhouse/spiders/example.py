# # -*- coding: utf-8 -*-
# import scrapy
# import requests
#
#
#
# header = {
#
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#     'Referer': 'http://hotel.elong.com/90960186/',
#     # 'Cookies': 'newjava1=4b8a89e07d1c72248e8f515c70663e7c; JSESSIONID=B31D2DDD8CCB81347D97C12CC73AFA73; CookieGuid=749be2ac-d7db-4764-b00b-8da7bbda9a4a; SessionGuid=0da3ef51-4053-42b2-80a6-7e197c29fa80; Esid=51f87678-6f2c-4208-b5d8-94597ad04205; com.eLong.CommonService.OrderFromCookieInfo=Orderfromtype=1&Parentid=50000&Status=1&Cookiesdays=0&Coefficient=0.0&Pkid=50&Priority=8000&Isusefparam=0&Makecomefrom=0&Savecookies=0; fv=pcweb; anti_token=C37B4ADD-6BB4-4FA1-954C-F4F96C5A9E4B; ext_param=bns%3D4%26ct%3D3; s_cc=true; s_visit=1; _fid=749be2ac-d7db-4764-b00b-8da7bbda9a4a; H5CookieId=f11e0a9a-ad30-4b06-8438-b1ba26c67727; __tctmb=0.4112251138507530.1557802585294.1557802585294.1; __tccgd=0.0; CitySearchHistory=0101%23%E5%8C%97%E4%BA%AC%23beijing%23; ShHotel=InDate=2019-05-14&CityID=0101&CityNameEN=beijing&CityNameCN=%E5%8C%97%E4%BA%AC&OutDate=2019-05-15&CityName=%E5%8C%97%E4%BA%AC; s_sq=%5B%5BB%5D%5D; SHBrowseHotel=cn=90960186%2C%2C%2C%2C%2C%2C%3B00401011%2C%2C%2C%2C%2C%2C%3B40101132%2C%2C%2C%2C%2C%2C%3B40101133%2C%2C%2C%2C%2C%2C%3B&; __tctmc=0.2396841; __tctmd=0.207648715',
#     'Cookie': 'newjava1=4b8a89e07d1c72248e8f515c70663e7c; CookieGuid=749be2ac-d7db-4764-b00b-8da7bbda9a4a; SessionGuid=0da3ef51-4053-42b2-80a6-7e197c29fa80; Esid=51f87678-6f2c-4208-b5d8-94597ad04205; com.eLong.CommonService.OrderFromCookieInfo=Orderfromtype=1&Parentid=50000&Status=1&Cookiesdays=0&Coefficient=0.0&Pkid=50&Priority=8000&Isusefparam=0&Makecomefrom=0&Savecookies=0; fv=pcweb; anti_token=C37B4ADD-6BB4-4FA1-954C-F4F96C5A9E4B; ext_param=bns%3D4%26ct%3D3; s_cc=true; _fid=749be2ac-d7db-4764-b00b-8da7bbda9a4a; H5CookieId=f11e0a9a-ad30-4b06-8438-b1ba26c67727; CitySearchHistory=0101%23%E5%8C%97%E4%BA%AC%23beijing%23; s_sq=%5B%5BB%5D%5D; SHBrowseHotel=cn=90960186%2C%2C%2C%2C%2C%2C%3B00401011%2C%2C%2C%2C%2C%2C%3B40101132%2C%2C%2C%2C%2C%2C%3B40101133%2C%2C%2C%2C%2C%2C%3B&; __tctmc=0.2396841; __tctmd=0.1; JSESSIONID=D775612E55B964A55D4C983A8E4A9A79; s_visit=1; ShHotel=InDate=2019-05-14&CityID=0101&CityNameEN=beijing&CityNameCN=%E5%8C%97%E4%BA%AC&OutDate=2019-05-15&CityName=%E5%8C%97%E4%BA%AC&; __tccgd=0.1; __tctmb=0.725403869386677.1557815945849.1557815945849.1',
#     'Origin': 'http://hotel.elong.com',
#     'Host': 'hotel.elong.com',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Accept': "*/*",
#     'Accept-Encoding': "gzip, deflate",
#     'Accept-Language': "zh-CN,zh;q=0.9",
#     'Connection': "keep-alive",
#     'Content-Length': "521",
#
# }
#
#
#
#
#
# url = 'http://hotel.elong.com/ajax/tmapidetail/gethotelroomsetjvajson'
#
# data = {"aBTestVersion":"old","bookingChannel":1,"cardNo":192928,"checkInDate":"2019-05-14","checkOutDate":"2019-05-15","customerLevel":11,
#         "hotelIDs":"90960186","isAfterCouponPrice":'true',"isDebug":'false',"isLogin":'false',"isMobileOnly":'false',"isNeed5Discount":'false',"isTrace":'false',"language":"cn","needDataFromCache":'true',"needPromotion":'true',"newABVersion":"Z","newVersion":'false',"orderFromID":50,"payMethod":0,"productType":0,"promotionChannelCode":"0000","proxyID":"ZD","sellChannel":1,"settlementType":0,"updateOrder":'false',"version":"G","elongToken":"749be2ac-d7db-4764-b00b-8da7bbda9a4a","code":6823833}
#
# import json
# info = json.loads(requests.post(url, headers=header, data=data).text)
#
# """ 网站是http://hotel.elong.com/90960186/"""
#
# print(info['hotelTipInfo']['productsInfo'][0]['priceOfDays'][0]['price'])
#
# print(info['hotelTipInfo']['hotelId'])
# from selenium import webdriver
#
# chromeOptions = webdriver.ChromeOptions()
#
# # 设置代理
# chromeOptions.add_argument("--proxy-server=http://112.65.52.112:4575")
# # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
# browser = webdriver.Chrome(chrome_options=chromeOptions)
#
# # 查看本机ip，查看代理是否起作用
# browser.get("http://httpbin.org/ip")
# print(browser.page_source)
#
#
# # 退出，清除浏览器缓存
# # browser.quit()
#
# import telnetlib
# try:
#   telnetlib.Telnet('61.132.93.14', port='41818', timeout=5)
# except:
#   print('connect failed')
# else:
#   print('success')
# #

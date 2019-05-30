# # # # import os
# # # # import asyncio
# # # # import traceback
# # # # from pyvirtualdisplay import Display
# # # #
# # # #
# # # # class XXX(object):
# # # #
# # # #     def __init__(self):
# # # #         self.logger = '日志实例化'
# # # #
# # # #     def crawl(self, name, uuid_TB):
# # # #         display = Display(visible=0, size=(800, 600))
# # # #         display.start()
# # # #         try:
# # # #             loop = asyncio.get_event_loop()
# # # #             ret_dict = loop.run_until_complete(self.run())
# # # #         except Exception as error:
# # # #             msg = ' [pid：{}] 爬虫 [{}] uuid_TB=[{}]程序出现错误：\ne = {}！'.format(
# # # #                 os.getpid(), name,
# # # #                 uuid_TB, error)
# # # #             self.logger.error(msg)
# # # #             self.logger.error(traceback.format_exc())
# # # #         finally:
# # # #             display.stop()
# # # #
# # #     async def run(self):
# # #         # 爬虫主逻辑
# # #         pass
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from pyvirtualdisplay import Display
DR = '/usr/local/bin/chromedriver'
display = Display(visible=0, size=(1024, 768))
display.start()
# driver = Chrome(executable_path=DR)
option = ChromeOptions()
# self.option.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option, executable_path=DR)
driver.get('http://hotel.elong.com/50301037/')
# a = driver.execute_script('return document.querySelector("#roomSetContainer")')
user4 = driver.execute_script("return window.navigator.webdriver;")
print('是否绕过无头检测', user4)
c = driver.page_source
print(c)
# display.stop()
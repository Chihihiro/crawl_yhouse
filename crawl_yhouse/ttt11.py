# # from selenium.webdriver import Chrome
# # from selenium.webdriver.chrome.options import Options
# #
# # # DRIVER_PATH = '/usr/local/bin/chromedriver'
# #
# #
# # if __name__ == "__main__":
# #     # 设置浏览器
# #     options = Options()
# #     options.add_argument('--no-sandbox')
# #     # options.add_argument('--headless')  # 无头参数
# #     options.add_argument('--disable-gpu')
# #     # 启动浏览器
# #     # driver = Chrome(options=options, executable_path=DRIVER_PATH)
# #     driver = Chrome(options=options)
# #     # 访问目标URL
# #     driver.get('http://hotel.elong.com/52001128/')
# #     print(driver.page_source)
# #     # driver.close()
# #     # driver.quit()
#
# import asyncio
# import pyppeteer
# import os
#
# os.environ['PYPPETEER_CHROMIUM_REVISION'] = '588429'
# pyppeteer.DEBUG = True
#
#
# async def main():
#     print("in main ")
#     print(os.environ.get('PYPPETEER_CHROMIUM_REVISION'))
#     browser = await pyppeteer.launch()
#     page = await browser.newPage()
#     await page.goto('http://www.baidu.com')
#
#     content = await page.content()
#     cookies = await page.cookies()
#     # await page.screenshot({'path': 'example.png'})
#     await browser.close()
#     return {'content': content, 'cookies': cookies}
#
#
# # loop = asyncio.get_event_loop()
# # task = asyncio.ensure_future(main())
# # loop.run_until_complete(task)
# #
# # print(task.result())
#
#
# # import os
# # os.system("taskkill/f/im chromedriver.exe")
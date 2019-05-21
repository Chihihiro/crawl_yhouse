# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
#
# DRIVER_PATH = '/usr/local/bin/chromedriver'
#
#
# if __name__ == "__main__":
#     # 设置浏览器
#     options = Options()
#     options.add_argument('--no-sandbox')
#     options.add_argument('--headless')  # 无头参数
#     options.add_argument('--disable-gpu')
#     # 启动浏览器
#     driver = Chrome(options=options, executable_path=DRIVER_PATH)
#     # 访问目标URL
#     driver.get('https://www.baidu.com/')
#     print(driver.page_source)
#     driver.close()
#     driver.quit()

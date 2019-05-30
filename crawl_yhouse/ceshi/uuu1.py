
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
from crawl_yhouse.proxy_pool import *
import random
import socket
from crawl_yhouse.user_agent import user_agent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pysnooper

option = ChromeOptions()
# self.option.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
option.add_experimental_option('excludeSwitches', ['enable-automation'])
prefs = {"profile.managed_default_content_settings.images": 2}
option.add_experimental_option("prefs", prefs)

option.add_argument('--no-sandbox')
option.add_argument('blink-settings=imagesEnabled=false')
option.add_argument('--disable-gpu')
# self.option.add_argument('--headless')
# self.option.add_argument('window-size=800x600')  # 指定浏览器分辨率
option.add_argument("--disable-dev-shm-usage")
option.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36')
# self.option.add_argument("--proxy-server=%s" % pp)
option.add_argument('-proxy-server=http://36.250.153.191:4561')
driver = Chrome(options=option)
driver.get('http://hotel.elong.com/50301037/')

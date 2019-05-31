from scrapy import cmdline
import os
os.system("ps -efww|grep Xvfb |grep -v grep|cut -c 9-15|xargs kill -9")

cmdline.execute("scrpay crawl yilong2".split())
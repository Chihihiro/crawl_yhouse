from scrapy import cmdline
cmdline.execute("scrpay crawl yilong".split())


import os
os.system("ps -efww|grep Xvfb |grep -v grep|cut -c 9-15|xargs kill -9")
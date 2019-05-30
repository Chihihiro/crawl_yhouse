
from scrapy import cmdline
import os
os.system("ps -efww|grep Xvfb |grep -v grep|cut -c 9-15|xargs kill -9")

cmdline.execute("scrpay crawlall".split())




from scrapy import cmdline
from scrapy.cmdline import execute
# import os
#
#
# os.system('scrpay crawl yilong')
# os.system('scrpay crawl yilong2')
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
from scrapy import cmdline
import os
os.system("ps -efww|grep Xvfb |grep -v grep|cut -c 9-15|xargs kill -9")

# cmdline.execute("scrpay crawl yilong2".split())


ss = ['scrapy crawl yilong', 'scrapy crawl yilong2']


def start_crawl(sysitem):
    print(sysitem)
    os.system(sysitem)


def main():
    pool = ThreadPool(16) #这个是多线程开启的话 就使用pool.map(start_crawl, ss)
    p = Pool(2) #这个是多进程
    result = p.map(start_crawl, ss)
    print('over')
    os.system("ps -efww|grep Xvfb |grep -v grep|cut -c 9-15|xargs kill -9")


if __name__ == "__main__":
    main()
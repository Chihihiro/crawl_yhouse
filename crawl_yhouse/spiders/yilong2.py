# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
import pandas as pd
from scrapy import Selector
import json
import time
from crawl_yhouse.items import CrawlYhouseItem
from crawl_yhouse.engines import choise_engine as engine





def get_id():
    sql = "select yhotel_id, return_id from yilong"
    df = pd.read_sql(sql, engine)
    y2y_id = dict(zip(df['return_id'], df['yhotel_id']))
    return y2y_id

def chang_time_all():
    timeStamp = time.time()
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime


def chang_time(int_time):
    timeStamp = int_time / 1000
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d")
    return otherStyleTime


from crawl_yhouse.ceshi.ll import lls

class YilongSpider(scrapy.Spider):
    name = 'yilong2'
    # allowed_domains = ['http://hotel.elong.com/92494775/']
    start_urls = [
                  # 'http://hotel.elong.com/52001128/',
                  # 'http://hotel.elong.com/91191052/',
                  # 'http://hotel.elong.com/90684208/',
                  # 'http://hotel.elong.com/50301037/',#这个很特别 需要单独处理
                  # 'http://hotel.elong.com/10201185/',
                  # 'http://hotel.elong.com/40201952/',
                  'http://hotel.elong.com/91855173/',
                  'http://hotel.elong.com/90602068/', #这个酒店就没有
                  'http://hotel.elong.com/40201044/',
                  'http://hotel.elong.com/10201082/',
                  'http://hotel.elong.com/50201055/',

                  ]

    # start_urls = lls



    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
           'crawl_yhouse.middlewares.CrawlYhouseDownloaderMiddleware': 543,
        },
        "ITEM_PIPELINES": {
            'crawl_yhouse.pipelines.CrawlYhousePipeline': 300,
        }
    }


    to_getid = get_id()







    def parse(self, response):


        print('到 parse了')
        print(response.status)
        # print(response.body)
        if response.status == 201:
            print(2011111111111)
        elif response.status == 200:
            yhouse_id = re.search('\d+', response.url).group()
            host_id = self.to_getid.get(yhouse_id)
            if host_id is None:
                host_id = '没有匹配到'

            print("*"*100)
            selector = Selector(response)
            no_hotel = selector.xpath('//*[@id="roomSetContainer"]/div/div/div/span/a/text()').extract()
            if len(no_hotel) == 1:
                print('此日期没有房间跳过~~~~~~~~')
                pass
            else:
                item = CrawlYhouseItem()
                item['hotel_id'] = yhouse_id
                item['host_id'] = host_id
                item['hotel_id'] = yhouse_id
                item['hotel_name'] = selector.xpath('/html/body/div[3]/div/div[1]/div[1]/div/h1/text()').extract()[0]
                checkin = selector.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/div[1]/label[1]/input/@value').extract()[0]
                checkout = selector.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/div[1]/label[2]/input/@value').extract()[0]
                item['checkout'] = checkout
                item['checkin'] = checkin


                rom = selector.xpath('//*[@id="roomSetContainer"]/div[2]/div/div')
                for i in range(len(rom)):
                    # 母房型级
                    room = rom[i].xpath('div[1]/div[3]/p[1]/span[1]/text()').extract()[0]
                    item['major_room_name'] = room
                    ll = rom[i].xpath('div[3]/table/tbody/tr')[0:-1]
                    item['bed_type'] = rom[i].xpath('div[1]/div[3]/p[2]/span[3]/text()').extract()[0]
                    item['network'] = rom[i].xpath('div[1]/div[3]/p[2]/span[9]/text()').extract()[0]
                    item['person'] = len(rom[i].xpath('div[1]/div[3]/p[2]/span[5]/i'))



                    for x in ll:
                        item['major_room_id'] = x.xpath('@data-mroomid').extract()[0]
                        item['minor_room_id'] = x.xpath('@data-sroomid').extract()[0]
                        item['minor_room_name'] = x.xpath('td[2]/span/text()').extract()[0]
                        item['breakfast'] = x.xpath('td[4]/text()').extract()[0]
                        item['policy'] = x.xpath('td[5]/p[1]/span/text()').extract()[0]
                        price = x.xpath('td[6]/span/span/text()').extract()[0]
                        price_point = x.xpath('td[6]/span/span/span/text()').extract()
                        if price:
                            item['price'] = price
                        else:
                            item['price'] = price + price_point[0]

                        # item['create_time'] = chang_time_all()

                        order_status = x.xpath('td[7]/span').extract()
                        if len(order_status) == 1:
                            order = 0
                        else:
                            order = 1
                        item['order_status'] = order
                        item['sou'] = 0
                        yield item



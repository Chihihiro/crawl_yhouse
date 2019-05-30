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


class YilongSpider(scrapy.Spider):
    name = 'yilong'
    # allowed_domains = ['http://hotel.elong.com/92494775/']
    start_urls = [
                  'http://hotel.elong.com/52001128/',
                  # 'http://hotel.elong.com/50301037/',
                  # 'http://hotel.elong.com/90684208/',
                  # 'http://hotel.elong.com/50301037/',#这个很特别 需要单独处理
                  # 'http://hotel.elong.com/10201185/',

                  #
                  # 'http://hotel.elong.com/40201010/',
                  # 'http://hotel.elong.com/40201952/',
                  # 'http://hotel.elong.com/91855173/',


                  # 'http://hotel.elong.com/10201307/',
                  # 'http://hotel.elong.com/40201044/',
                  # 'http://hotel.elong.com/10201082/',
                  # 'http://hotel.elong.com/50201055/',
                  # 'http://hotel.elong.com/40201192/',
                  # 'http://hotel.elong.com/50201284/',
                  # 'http://hotel.elong.com/50201261/',
                  # 'http://hotel.elong.com/50201481/',
                  # 'http://hotel.elong.com/00101108/',
                  # 'http://hotel.elong.com/40301051/',
                  # 'http://hotel.elong.com/00101972/',
                  # 'http://hotel.elong.com/40101839/',
                  # 'http://hotel.elong.com/40101676/',
                  ]



    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
           'crawl_yhouse.middlewares.CrawlYhouseDownloaderMiddleware': 543,
        },
        "ITEM_PIPELINES": {
            'crawl_yhouse.pipelines.CrawlYhousePipeline': 300,
        }
    }

    # to_getid = get_id()

    #
    # def parse(self, response):
    #     print('到 parse了')
    #     print(response.status)
    #     # print(response.body)
    #     if response.status == 201:
    #         print(2011111111111)
    #     elif response.status == 200:
    #         yhouse_id = re.search('\d+', response.url).group()
    #         print(yhouse_id)
    #         info = json.loads(response.body)
    #         print(info['hotelTipInfo']['hotelId'])
    #         yilong_id = info['hotelTipInfo']['hotelId']
    #         if yilong_id ==yhouse_id:
    #             print('请求成功拿到正确id')
    #         #     item = CrawlYhouseItem()
    #         #     host_id = self.to_getid.get(yhouse_id)
    #         #     item['host_id'] = host_id
    #         #     item['hotel_id'] = yhouse_id
    #         #     item['hotel_name'] = info['hotelInventory']['hotelName']
    #         #     rooms_house = info['hotelInventory']['rooms']
    #         #     checkin = info['hotelInventory']['detailRequest']['checkInDate']
    #         #     item['checkin'] = chang_time(checkin)
    #         #     checkout = info['hotelInventory']['detailRequest']['checkOutDate']
    #         #     item['checkout'] = chang_time(checkout)
    #         #     for mother_room in rooms_house:
    #         #         # 母房型级
    #         #         item['major_room_id'] = mother_room['roomTypeID']#母房型ID
    #         #         item['major_room_name'] = mother_room['roomTypeName']
    #         #         item['bed_type'] = mother_room['bedTypeName']
    #         #         item['network'] = mother_room['networkDesc']
    #         #         for room in mother_room['allProductList']:
    #         #             item['minor_room_name'] = room['ratePlanName']
    #         #             item['minor_room_id'] = room['sRoomTypeID']
    #         #             item['breakfast'] = room['breakfastDesc']
    #         #             item['policy'] = room['cancelRuleDesc']
    #         #             item['person'] = room['maxPerson']
    #         #             item['price'] = room['avgPrice']
    #         #             item['create_time'] = chang_time_all()
    #         #             item['order_status'] = room['enableBook']
    #         #             item['sou'] = 0
    #         #             yield item
    #         else:
    #             print('ID不相同')
    #         #     pass
    #         pass
    #     else:
    #         pass





    def parse(self, response):


        print('到 parse了')
        print(response.status)
        # print(response.body)
        if response.status == 201:
            print(2011111111111)
        elif response.status == 200:
            url_id = re.search('\d+', response.url).group()
            item = CrawlYhouseItem()
            item['hotel_id'] = url_id
            # print(response.body)
            print("*"*100)
            selector = Selector(response)
            # rom4 = selector.xpath('//*[@id="roomSetContainer"]/div[2]/div[1]/div')
            rom4 = selector.xpath('//*[@id="roomSetContainer"]/div[2]/div/div')
            for i in range(len(rom4)):
                room = rom4[i].xpath('div[1]/div[3]/p[1]/span[1]/text()').extract()[0]
                item['minor_room_name'] = room
                ll = rom4[i].xpath('div[3]/table/tbody/tr')[0:-1]
                print(len(ll))
                for x in ll:
                    plice = x.xpath('td[6]/span/span/text()').extract()[0]
                    print(plice)
                    item['plice'] = plice
                    print(item)
                    # yield item
                    pass






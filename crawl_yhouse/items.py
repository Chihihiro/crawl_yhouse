# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlYhouseItem(scrapy.Item):
    host_id = scrapy.Field()
    hotel_id = scrapy.Field()
    hotel_name = scrapy.Field()
    major_room_id = scrapy.Field()
    major_room_name = scrapy.Field()
    minor_room_id = scrapy.Field()
    minor_room_name = scrapy.Field()
    bed_type = scrapy.Field()
    breakfast = scrapy.Field()
    network = scrapy.Field()
    person = scrapy.Field()
    policy = scrapy.Field()
    price = scrapy.Field()
    plice = scrapy.Field()
    checkin = scrapy.Field()
    checkout = scrapy.Field()
    create_time = scrapy.Field()
    order_status = scrapy.Field()
    sou = scrapy.Field()
    pass

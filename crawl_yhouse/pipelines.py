# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pandas as pd
import re
from crawl_yhouse.items import *
from crawl_yhouse.engines import choise_engine



def dff_df(df):
    df2 = df.T
    df4 = df2[df2[0] != ""]
    dff = df4.T
    return dff



def clean3(str1):
    try:
        sst = re.search('<(.+?)>', str1).group()
    except AttributeError:
        return str1
    last_str = re.sub('%s|</b>' % sst, '', str1)
    return last_str



TABLE_DICT = {
    CrawlYhouseItem: 'ctrip_room_info_test',

}
from crawl_yhouse.iosjk import to_sql


class CrawlYhousePipeline(object):
    def process_item(self, item, spider):
        # print(type(item))
        table = TABLE_DICT.get(type(item))
        df = pd.DataFrame([dict(item)])
        # df['order_status'] = df['order_status'].apply(lambda x: 1 if x == True else 0)
        # df['policy'] = df['policy'].apply(lambda x: clean3(x))
        # clean_df = for_columns(df)
        to_sql(table, choise_engine, df, type="update")
        return item



# import re
# import json
# import time
# import pandas as pd
# import sys
# import time
# import datetime
# import numpy as np
# import pysnooper
# from sqlalchemy import create_engine
# from crawl_yhouse.iosjk import to_sql
# import requests
# from crawl_yhouse.user_agent import list_header
# from urllib import request
#
#
# engine_config_private = create_engine(
#     "mysql+pymysql://{}:{}@{}:{}/{}".format('spider_dev', 'csQXEMw9udrC4f*4JB6WnGiv2MKZRn', 'localhost', 13306,
#                                             'yhouse', ), connect_args={"charset": "utf8"}, echo=True, )
# my_engine = create_engine(
#     "mysql+pymysql://{}:{}@{}:{}/{}".format('root', 'chihiro123', '47.107.35.189', 3306,
#                                             'spider', ), connect_args={"charset": "utf8"}, echo=True, )
#
#
#
#
#
#
#
# def re_word(word):
#     first_word = request.quote(word)
#     end_word = first_word.replace('%', '%25')
#     return end_word
#
#
# def max_list(lt):
#     temp = 0
#     for i in lt:
#         if lt.count(i) > temp:
#             max_str = i
#             temp = lt.count(i)
#     return max_str
#
#
# def get_city(word):
#     ulr = f"http://www.elong.com/ajax/search/desautosug/?keys={re_word(word)}&_={str(int(time.time() * 1000))}"
#     header = {'User-Agent': list_header}
#     info = json.loads(requests.get(ulr, headers=header).text)
#     ll = []
#     for i in range(len(info)):
#         # print(info[i]['destId'],info[i]['destChName'])
#         ll.append(str(info[i]['destId'])+info[i]['destChName'])
#     max_word = max_list(ll)
#     all_word = ",".join(ll)
#     are = str(re.compile('\d+').search(max_word).group()).zfill(4)
#     city_all = [word, are, max_word, all_word]
#     return city_all
#
#
# def write(ll_cits):
#     """传入城市list"""
#     df_list = []
#     for i in ll_cits:
#         df_list.append(get_city(i))
#     df = pd.DataFrame(df_list)
#     df.columns = ['word', 'area', 'max_word', 'all_word']
#     to_sql('city', my_engine, df, type='update')
#
#
#
#
# @pysnooper.snoop()
# def look(df):
#     # df.to_excel('C:\\Users\\xiaod\\Desktop\\lookhouse.xlsx')
#     ll = list(set(list(df['name'].values)))
#     print(len(ll))
#     print(ll[0])
#     return ll[0]
#
#
#
# get_sql = "select word, area from city"
# get_df = pd.read_sql(get_sql, my_engine)
# city_dict = dict(zip(get_df['word'], get_df['area']))
#
#
# sql = "SELECT DISTINCT \
#         a.id, \
#         a.host_name, \
#         c.`name` \
#         from host_info a \
#         JOIN hotel_supplier_mapping b on a.id = b.yhouse_hotel_id \
#         JOIN base_city c on a.city_id = c.id"
# # df = pd.read_sql(sql, engine_config_private)
# # df['area_id'] = df['area_id'].apply(lambda x: str(x).zfill(4))
# # print(df)
#
# #
# # all_hotel = np.array(df).tolist()
# # all_hotel2 = all_hotel[::-1]
# # # city_word = '杭州雷迪森铂丽大饭店'
# # # area = city_dict.get('杭州')
# #
# # # sky_hotel = []
# # for i in all_hotel2:
# #     try:
# #         city_word = i[1]
# #         area = city_dict.get(i[2])
# #         # url = f"http://hotel.elong.com/ajax/search/suggest?cityId=1614&keyword="
# #         # url = f'http://hotel.elong.com/ajax/search/suggest?cityId=1614&keyword=%25E6%259D%25AD%25E5%25B7%259E%25E9%259B%25B7%25E8%25BF%25AA%25E6%25A3%25AE%25E9%2593%2582%25E4%25B8%25BD%25E5%25A4%25A7%25E9%25A5%25AD%25E5%25BA%2597'
# #         url = f"http://hotel.elong.com/ajax/search/suggest?cityId={area}&keyword={re_word(city_word)}"
# #         print(url)
# #         header = {'User-Agent': list_header}
# #         info = json.loads(requests.get(url, headers=header).text)
# #         print(info)
# #         try:
# #             hotel = info['keyword_response'][0]['name']
# #             print(hotel)
# #             hotel_id = info['keyword_response'][0]['elongHotelId']
# #             print(hotel_id)
# #         except:
# #             hotel = '沒有匹配到'
# #             hotel_id = '没有匹配到'
# #         hotel_all = [i[0], i[1], hotel, hotel_id, i[2], area]
# #         print(hotel_all)
# #         # sky_hotel.append(hotel_all)
# #
# #         hotel_df = pd.DataFrame(hotel_all).T
# #         hotel_df.columns =['yhotel_id', 'search_name', 'return_name', 'return_id', 'city', 'city_id']
# #         to_sql('yilong', my_engine, hotel_df, type='update')
# #     except BaseException as e:
# #         print(e)
#
#
#
#
# # ll = []
# # for i in range(len(info)):
# #     # print(info[i]['destId'],info[i]['destChName'])
# #     ll.append(str(info[i]['destId']) + info[i]['destChName'])
# # max_word = max_list(ll)
# # all_word = ",".join(ll)
# # are = str(re.compile('\d+').search(max_word).group()).zfill(4)
# # city_all = [word, are, max_word, all_word]
#
#
# xlsx_sql = "select * from yilong"
#
# df = pd.read_sql(xlsx_sql, my_engine)
#
# df['web'] = df['return_id'].apply(lambda x: f"http://hotel.elong.com/{x}/")
# print(df)
#
#
# df.to_excel('C:\\Users\\xiaod\\Desktop\\yilong_house.xlsx')
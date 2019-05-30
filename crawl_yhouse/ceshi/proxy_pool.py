# # -*- coding: utf-8 -*-
#
# import redis
#
# from conf.base_conf import PROXY_POOL_NAME
# from conf.dbconf import REDIS_SETTINGS
#
#
# class ProxyPool(object):
#     def __init__(self, num, name=PROXY_POOL_NAME, db_settings=REDIS_SETTINGS):
#         self._client = redis.Redis(**db_settings)
#         self._name = name + num
#
#     def put(self, *data):
#         """ append proxy to pool."""
#         self._client.rpush(self._name, *data)
#
#     def pop(self):
#         """ get one proxy from pool."""
#         return self._client.lpop(self._name)
#
#     def flush(self):
#         """ delete proxy pool."""
#         self._client.delete(self._name)
#
#     def get(self, count=1):
#         """ get proxies range from left."""
#         return self._client.lrange(self._name, 0, count - 1)
#
#     def trim(self, start, end):
#         """ trim pool."""
#         self._client.ltrim(self._name, start, end)
#
#     def __len__(self):
#         return self._client.llen(self._name)
#
#
# for i in range(3):
#     pool = ProxyPool(str(i + 1))
#
#     length = len(pool)
#     if length > 100:
#         pool.trim(length - 50, -1)
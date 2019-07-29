# -*- coding: utf-8 -*-
"""
IP代理池
受限于第三方代理的白名单
一个代理通道只支持3个访问IP白名单
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import socket
import time
from datetime import datetime
import random
import redis



local = dict(
    host='localhost',
    port=10001,
    db=1,
    decode_responses=True,
)


REDIS_SETTINGS = dict(
    host='10.10.53.221',
    port=6379,
    db=1,
    decode_responses=True,
)





class ProxyPool(object):
    __slots__ = ('__name', '__client', '__interval')

    def __init__(self):
        hostname = socket.gethostname()

        if hostname in ('wx09', 'wx01', 'wx02'):
            self.__name = 'ip_proxy1'
        elif hostname in ('wx03', 'wx04', 'wx05'):
            self.__name = 'ip_proxy2'
        elif hostname in ('wx06', 'wx07', 'wx08'):
            self.__name = 'ip_proxy3'
        elif hostname in ('DESKTOP-6UPQ2C9', 'chihiro'):
            self.__name = 'ip_proxy1'
        else:
            raise RuntimeError('hostname {} is not illegal.'.format(hostname))

        if hostname in ('DESKTOP-6UPQ2C9', 'chihiro'):
            self.__client = redis.Redis(**local)
        else:
            self.__client = redis.Redis(**REDIS_SETTINGS)

        self.__interval = 10

    @property
    def name(self):
        return self.__name

    @property
    def interval(self):
        return self.__interval

    def put(self, *data):
        """ append proxy to pool."""
        self.__client.rpush(self.__name, *data)

    def pop(self, flag=''):
        """ get one proxy from pool."""
        if not flag:
            # no process flag
            # get proxy from left, then put it back on right
            data = self.__client.lpop(self.__name)
            if data is not None:
                self.put(data)
            return data
        else:
            data = self.__client.lpop(self.__name)
            if data is None:
                return data

            proxy = json.loads(data)

            if not proxy.get(flag):
                proxy[flag] = True
                data = json.dumps(proxy)
                self.put(data)
                return data
            else:
                self.put(data)
                return self.pop(flag)

    def flush(self):
        """ delete proxy pool."""
        self.__client.delete(self.__name)

    def get(self, count=1):
        """ get proxies range from left."""
        return self.__client.lrange(self.__name, 0, count - 1)

    def trim(self, start, end):
        """ trim pool."""
        self.__client.ltrim(self.__name, start, end)

    def __len__(self):
        return self.__client.llen(self.__name)

    def get_proxy(self):
        data = self.pop()

        if data is not None:
            meta = json.loads(data).get('http')
            return {'http': meta, 'https': meta}
        else:
            time.sleep(self.__interval)
            return self.get_proxy()



http_proxy = ProxyPool().get_proxy().get('http')[7:]
# print(http_proxy)
# print(socket.gethostname())


# -*- coding: utf-8 -*-
from crawl_yhouse.ceshi.proxy_pool import ProxyPool

for i in range(3):
    pool = ProxyPool(str(i + 1))

    length = len(pool)
    if length > 100:
        pool.trim(length - 50, -1)

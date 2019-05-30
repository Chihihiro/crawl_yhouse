import random, base64
from crawl_yhouse.proxy_pool import *

class ProxyMiddleware(object):

    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = ProxyPool().get_proxy().get('http')[7:]

        print("USE PROXY -> " + pro_adr)
        request.meta['proxy'] = "http://" + pro_adr
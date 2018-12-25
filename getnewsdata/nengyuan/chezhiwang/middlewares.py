# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from chezhiwang import items
import scrapy
import random
from scrapy import log
import time
class ChezhiwangSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ChezhiwangDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



import random
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware #代理ip，这是固定的导入
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware #代理UA，固定导入
class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        '''初始化'''
        self.ip=ip
    def process_request(self, request, spider):
        '''使用代理ip，随机选用'''
        ip=random.choice(self.ip_pools) #随机选择一个ip
        print ('当前使用的IP是'+ip['ip'])
        try:
            request.meta["proxy"]="http://"+ip['ip']
        except (Exception):
            #print (e)
            pass
    ip_pools=[

        {'ip':'121.69.37.6:9797'},
        {'ip': '118.122.92.252:37901'}
        #{'ip':'59.172.27.6:53281'}

        #https
        # {'ip': '27.54.248.42:8000'},
        # {'ip':'118.122.92.252:37901'},
        # {'ip': '120.69.82.110:44693'}
        #{'ip':'119.39.68.57:808'}
    ]
class UAPOOLS(UserAgentMiddleware):
    def __init__(self,user_agent=''):
        self.user_agent=user_agent
    def process_request(self, request, spider):
        '''使用代理UA，随机选用'''
        ua=random.choice(self.user_agent_pools)
        print ('当前使用的user-agent是'+ua)
        try:
            request.headers.setdefault('User-Agent',ua)
        except (Exception):

            pass
    user_agent_pools=[
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
    ]
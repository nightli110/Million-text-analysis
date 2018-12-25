from scrapy.spider import BaseSpider
from chezhiwang.arrangurl import *
from chezhiwang import items
from chezhiwang import myre
class DmozSpider(BaseSpider):
    name = "zhongche"
    allowed_domains = ["chinanews.cn"]
    # start_urls = [
    #     "http://www.chinanews.cn/jk/kong/news/2008/08-01/1332750.shtml"
    # ]
    start_urls=arrangeurl('yule','health')
    def parse(self, response):
        #self.log("title:%s"%response.css('div.title0').extract())
        title=response.css('div.title0').extract()
        title=str(title)
        if title=='[]':#left_bt
            title = response.css('div.left_bt').extract()
        title=myre.cleancode(str(title))
        text=response.css('div.left_zw').extract()
        if text==[]:
            text = response.css('div.font16Style').extract()
        text=str(text)
        if text=='':
            text = response.css('div.left_zw').extract()
        text = myre.cleancode(text)
        type='yule'
        myitem=items.ChezhiwangItem()
        myitem['title']=title
        myitem['text_content']=text
        myitem['type']=type
        # yield {
        #     'title': title,
        #     'text_content': text,
        #     'type':type
        # }
        yield myitem

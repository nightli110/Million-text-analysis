# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
class TutorialPipeline(object):

    def __init__(self):

        dbargs = dict(
            host = 'localhost' ,
            db = 'pa_db',
            user = 'root', #replace with you user name
            passwd = '123456', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
            )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)


    '''
    The default pipeline invoke function
    '''
    def process_item(self, item,spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item

    def insert_into_table(self,conn,item):
        #conn.execute('insert into zreading(title,content,tytle) values(%s,%s,%s)', (item['title'],item['text_content'],'haha'))
        #print('insert into jiankang(title,content) values(%s,%s)',(item['title'],item['text_content']))
        title=str(item['title'])
        text=str(item['text_content'])
        type=str(item['type'])
        conn.execute('insert into yule2(title,content,type) values(%s,%s,%s)', (title, text,type))

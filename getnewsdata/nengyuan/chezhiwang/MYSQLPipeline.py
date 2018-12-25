import MySQLdb
class MySQLPipeline:
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'pa_db')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'root')
        self.db_conn = MySQLdb.connect(host='localhost', port=3306, db='pa_db',
        user='root', passwd='123456', charset='utf8')
        self.db_cur = self.db_conn.cursor()
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()
    def process_item(self, item, spider):
        self.insert_db(item)
        return item
    def insert_db(self, item):
        values = (
            item['title'],
            item['text_content'],
            item['type'],

            )
        print('hh')
        sql = 'INSERT INTO jiankang VALUES (%s,%s,%s)'
        self.db_cur.execute(sql, values)
import datetime
#Tempurl is the address of China News Network, 
#http://www.chinanews.com/scroll-news/+type+/year+/date+/new.shtml
#example:http://www.chinanews.com/scroll-news/it/2010/1201/news.shtml'
def get_data_list(start,end):
    url_date_list=[]
    date_start=datetime.datetime.strptime(start,'%Y-%m-%d')
    date_end=datetime.datetime.strptime(end,'%Y-%m-%d')
    while date_start<=date_end:
        temptime=date_start.strftime('/%Y/%m%d')
        tempurl='http://www.chinanews.com/scroll-news/it'+temptime+'/news.shtml'
        url_date_list.append(tempurl)
        date_start=date_start+datetime.timedelta(1)
    return url_date_list

#url_list=get_data_list('2008-08-01','2018-11-19')

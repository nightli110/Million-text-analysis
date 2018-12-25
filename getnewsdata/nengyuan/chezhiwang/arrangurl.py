# _*_coding:utf-8_*_
import csv
def arrangeurl(textname,type):
    csv_name=textname+'.csv'
    csvfile=open(csv_name,'r')
    csvfile=csv.reader(csvfile)
    content=[]
    urllist = []
    for line in csvfile:

        temp=line[1]#.replace(type,'www')
        urllist.append(temp)
    return urllist


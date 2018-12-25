# Million-text-analysis
 Million text analysis，from get million text data，Pretreatment text data to text data classification
 my data from China News Network https://www.chinanews.com/
## This project contains three parts：
1. get data
2. Pretreatment data
3. classify data
## environment
1. python 3.5
2. xgboost
3. sklearn
4. numpy
5. Scipy
6. selenium
7. Scrapy
8.mysql
9. ......
## first: get news data
Get the url information of the crawl news 
```
 cd geturllist
 python geturllist.py
```
<br>the news urllist url Have a certain law：</br>
<br>http://www.chinanews.com/scroll-news/+type+/+year+/+month+day+/+news.shtml<\br>
<br>example:http://www.chinanews.com/scroll-news/it/2012/1201/news.shtml<\br>
<br>then use these url to get news content
<br>use Scrapy to get news and mysql to store data
<br>Mysql configuration is in \getnewsdata\nengyuan\chezhiwang\pipelines
<br>there is a spider zhongche.py
<br>I get about 1.9 millon news
## Second：Pretreatment data
Read mysql data and Participle

```
python getword.py
```
I use jieba to Participle
there is a train_text.txt example in mynews
```
python chuli3.py
```
to remove some words
## classify data
first 
```
cd Classifier
python news_Bayes.py
```
to get tfidf feature and bayes classification
your should read code to build folder
```
python news_XGBoost.py
```
to use XGBoost classification
## the acc about my get news data is 94%
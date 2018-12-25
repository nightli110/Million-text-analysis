from selenium import webdriver
import time
import csv
from getdate import *
def save_result(find_result,textresult):
    csv_file=open('tiyu.csv','a',newline='')
    csv_write = csv.writer(csv_file, dialect='excel')
    for result in find_result:

        if result.get_attribute('href') not in textresult:
            temp_text=result.text
            temp_href=result.get_attribute('href')
            temp_out=[temp_text,temp_href]
            try:
                {
                    csv_write.writerow(temp_out)
                }
            except(UnicodeError, UnicodeDecodeError, UnicodeEncodeError, UnicodeTranslateError):
                continue
            textresult.append(temp_href)
    return textresult




chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser=webdriver.Chrome(chrome_options=chrome_options)
url_list=get_data_list('2011-11-09','2018-11-19')
js="var q=document.documentElement.scrollTop=1000000000000000"
textresult=[]
num=len(textresult)
save_num=4
for url in url_list:
    browser.get(url)
    #browser.execute(js)
    time.sleep(0.5)
        #find_next=browser.find_element_by_css_selector('div.news_lookmore>div>div').click()

    print("now len num"+str(len(textresult)))
    find_results=browser.find_elements_by_css_selector('div.content_list>ul>li>div>a')
    textresult=save_result(find_results,textresult)

    #next_href = browser.find_elements_by_css_selector('div.MBL>div>a.a1')
    #next_href=next_href[2].get_attribute('href')
    #browser.implicitly_wait(10)
    #browser.get(next_href)
    #num=len(textresult)

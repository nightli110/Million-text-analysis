import sklearn
import jieba
import jieba.analyse
import jieba.posseg as pseg
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from chuli import *
typelist=['健康','军事','国际','IT','娱乐','能源','体育','房产','证券','文化']
content_class=[[] for i in range (len(typelist))]
lablelist=[]
textlist=[]
test_file=open('mynews/text_train.txt','r',encoding='utf-8')
content=test_file.readlines()
for i in content:
    i=i.split('\t')
    lablelist.append(i[0])
    textlist.append(i[1])
for i in range(0,len(lablelist)):
    lable=lablelist[i]
    lable_index=typelist.index(lable)
    content_class[lable_index].append(textlist[i])
#keywords=jieba.analyse.extract_tags(test_file.read(),topK=20)
#print(keywords)
stopword_list=stop_word()
jiankang=''
for i in range(0,10):
    out_text_name = 'out2/' + typelist[i] + '.txt'
    fo = open(out_text_name, 'w', encoding='utf-8')
    for j in range(0,len(content_class[i])):
    #for j in range(0, 10000):
    # tempstr=content_class[0][i]
    # temp=jieba.cut(content_class[0][i])
    # temp=clean_stop(temp,stopword_list)
    # #print(",".join(temp))
    # print(i)
        jiankang=content_class[i][j]

        temp=pseg.cut(jiankang)
        temp_add=[]

    #temp=clean_stop(temp,stopword_list)
        for ele in temp:
            if ele.flag=='n' or ele.flag=='nz' or ele.flag=='nt' or ele.flag=='v':
                temp_add.append(ele)
        strout=qubiaodian(temp_add)

        fo.write(strout)
    fo.close()
    jiankang = ''


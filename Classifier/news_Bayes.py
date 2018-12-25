import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
from sklearn.model_selection import train_test_split
from scipy import sparse
import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
typelist=['健康','军事','国际','IT','娱乐','能源','体育','房产','证券','文化']
train=[]
label=[]
#getdata
for i in typelist:
    path='out3/'+i+'.txt'
    file=open(path,'r',encoding='utf-8').readlines()
    num=typelist.index(i)
    for line in file:
        train.append(line)
        label.append(num)

x_train,x_test,y_train,y_test=train_test_split(train,label,test_size=0.5,random_state=3)
#Get tfidf feature and save
cv=ft.CountVectorizer(max_features = 10000)
train_tfmat = cv.fit_transform(x_train)
test_tfmat = cv.transform(x_test)
np.save('feature_10000/train_label.npy',y_train)
np.save('feature_10000/test_label.npy',y_test)
sparse.save_npz('feature_10000/train.npz',train_tfmat)
sparse.save_npz('feature_10000/test.npz',test_tfmat)
#load feature to optimization
#train_tfmat=sparse.load_npz('feature_10000/train.npz')
#test_tfmat=sparse.load_npz('feature_10000/test.npz')
#y_train=np.load('feature_10000/train_label.npy')
#y_test=np.load('feature_10000/test_label.npy')
#print(train_tfmat.shape)
tf = ft.TfidfTransformer()
train_x = tf.fit_transform(train_tfmat)
print(1)
model = nb.MultinomialNB()
model.fit(train_x,y_train)

test_x = tf.transform(test_tfmat)
pred_test_y = model.predict(test_x)
c=0
e=0
acc=0
pred_test_y=list(pred_test_y)
for i in range(0,len(pred_test_y)):
    if int(y_test[i])==int(pred_test_y[i]):
        c=c+1
    else:
        e=e+1
    acc=c/(c+e)
    print('c:  '+str(c)+'   e:  '+str(e)+'  acc:  '+str(acc))
acc=precision_score(y_test,pred_test_y,average=None)
recall=recall_score(y_test,pred_test_y,average=None)
for i in range(0,10):
    tempstr=typelist[i]+'的准确率为：'+str(acc[i])+'  召回率为：'+str(recall[i])
    print(tempstr)
print('1')

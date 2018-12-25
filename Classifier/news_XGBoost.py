import xgboost as xgb
from xgboost import plot_importance
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from scipy import sparse
import numpy as np
y_test=np.load('feature_10000/test_label.npy')
test_vecs=sparse.load_npz('feature_10000/test.npz')
dtest=xgb.DMatrix(test_vecs,label=y_test)
typelist=['健康','军事','国际','IT','娱乐','能源','体育','房产','证券','文化']

param = {'max_depth': 4, 'eta': 0.05, 'silent': 0,'objective': 'multi:softmax','num_class':10,'lambda': 1}
param['nthread'] = -1
param['min_child_weight']=6
param['eval_metric'] = 'merror'
param['subsample']=1
bst=xgb.Booster(model_file='0001.model')
preds = bst.predict(dtest)
accuracy = accuracy_score(y_test, preds)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
acc=precision_score(y_test,preds,average=None)
recall=recall_score(y_test,preds,average=None)
for i in range(0,10):
    tempstr=typelist[i]+'的准确率为：'+str(acc[i])+'  召回率为：'+str(recall[i])
    print(tempstr)

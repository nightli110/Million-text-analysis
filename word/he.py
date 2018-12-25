typelist=['健康','军事','国际','IT','娱乐','能源','体育','房产','证券','文化']
content=[]
label=[]
for i in typelist:
    path='out3/'+i+'.txt'
    file=open(path,'r',encoding='utf-8').readlines()
    num=typelist.index(i)
    for line in file:
        content.append(line)
        label.append(num)
    print(num)
content_file='he/'+'content'+'.txt'
label_file='he/'+'label'+'.txt'
content_text=open(content_file,'w',encoding='utf-8')
label_text=open(label_file,'w',encoding='utf-8')
for line in content:
    content_text.writelines(line)
for line in label:
    label_text.write(str(line))
#content_text.writelines(content)
#label_text.writelines(label)
content_text.close()
label_text.close()
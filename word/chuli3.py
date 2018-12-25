typelist=['健康','军事','国际','IT','娱乐','能源','体育','房产','证券','文化']
for i in typelist:
    path='out2/'+i+'.txt'
    outpath='out3/'+i+'.txt'
    file=open(path,'r',encoding='utf-8').readlines()
    outfile=open(outpath,'w',encoding='utf-8')
    i=0
    for line in file:
        i=i+1
        print(i)
        line=line.split(' ')

        out_temp=[]
        for charitem in line:
            if len(charitem)>1:
                out_temp.append(charitem)

        # stdout=''.join(out_temp)
        stdout=''
        for charitem in out_temp:
            stdout=stdout+' '+charitem
        outfile.write(stdout)
    outfile.close()


from gensim.models import word2vec
import gensim
import logging
def stop_word():
    stop_word_file=open('mynews/cnews.vocab.txt','r',encoding='utf-8')
    stopword_list=[]
    for line in stop_word_file.readlines():
        line=line.strip('\n')
        stopword_list.append(line)
    return stopword_list

def clean_stop(segs,stoplist):
    return_out=[]
    for seg in segs:
        if seg not in stoplist:
            return_out.append(seg)

    return return_out


def qubiaodian(textin):
    str_out = ' '.join(textin).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
        .replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
        .replace('’', '')
    return str_out
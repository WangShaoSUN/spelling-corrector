#encoding=utf-8
from __future__ import division
import re
import collections
# print str("dd")
def edit(word):
    ''''
       寻找相似单词
    '''
    letters= 'abcdefghijklmnopqrstuvwxyz'
    splits=[(word[:i],word[i:]) for i in range(len(word)+1)]
    deletes=[head+tail[1:] for head,tail in splits if tail]  #词分成两部分,去掉一个词的所有结果\
    swaps=[head+swap[1]+swap[0]+swap[2:] for head,swap in splits if len(swap)>=2] #交换单词中相邻单词的位置
    replaces=[head+c+tail[1:] for head,tail in splits if tail for c in letters]
    inserts=[head+c+tail for head,tail in splits for c in letters]

    # print splits
    # print deletes
    # print  swaps
    # print replaces
    # print inserts
    return set(deletes+swaps+replaces+inserts)

# print(len(edit("somthing")))


def dic(text):
    words= re.findall('[a-z]+',text.lower())
    dic=collections.Counter(words)
    sum_words=sum(dic.values())
    print  dic.most_common()
    return dic,sum_words
fd=open("/home/wang/PycharmProjects/project/spelling correcter/words.txt")
dictornary,N=dic(fd.read())
def Bayes(word):
    # fd=open("/home/wang/PycharmProjects/project/spelling correcter/words.txt")
    # dictornary,N=dic(fd.read())
    def P(word):
        print dictornary[word],N
        return dictornary[word]/N
    candidate=edit(word)
    finalwords=[w for w in candidate if w in dictornary]
    # print "候选词",finalwords
    d={}
    for i in finalwords:
        d[i]=P(i)
    # print d
    d=sorted(d.items(),key=lambda x:x[1],reverse=True)

    print d
    print dictornary["ha"]
    # print P("unmentioned")


# words= re.findall('[a-z]+',"*asdf ff124fdff")
# print words
Bayes("word")


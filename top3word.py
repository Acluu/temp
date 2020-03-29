import re
def top_3_words(text):
    wordlist=[i for i in text.replace(',',' ').replace('.',' ').replace(':',' ').replace('\\','').replace('/',' ').lower().split() if bool(re.search('[a-z]',i))]    
    worddict={}
    for i in set(wordlist):
        worddict[i]=0
    for word in wordlist:
        worddict[word]+=1    
    test=[i[0] for i in sorted(worddict.items(),key=lambda x:x[1],reverse=True)]
    if len(test)<=3:
        return test
    else:
        return test[:3]
    

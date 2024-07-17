import sys

def spliting_and_counting(data):
    wordlist = data.split(" ")
    wordict={}
    for i in wordlist:
        try:
            wordict[i]+=1
        except:
            wordict[i]=1
    
    return wordict

def prinnting(sortedict,amount):
    count=0
    for i in sortedict:
        if amount>count:
            print(count+1,"- the word ",i,"was written ",sortedict[i],"times")
        count+=1
    

if __name__=='__main__':
    with open('D:\מועדון_המתכנתים\just_a_text_file.txt','r') as f:
        data=f.read()
    wordict=spliting_and_counting(data)
    sortedict=dict(sorted(wordict.items() , key=lambda item: item[1],reverse=True))
    prinnting(sortedict,2)
    
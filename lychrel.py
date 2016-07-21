from multiprocessing import Pool
from contextlib import closing
import time
nonLychrel=[]
def addTwoStrings(x,y): #going to assume they are of equal length
    carry=0
    result=''
    for i in range(len(x)):
        a=ord(x[i])-48
        b=ord(y[i])-48
        sum=a+b+carry
        if(sum>=10):
            carry=sum/10
            sum=sum%10
        else:
            carry=0
        result=str(sum)+result
    if carry>0:    
        result=str(carry)+result
    return result
def isLychrelHash(x):
    n=0
    l=[]
    global nonLychrel
    while(n<=50):
        n=n+1
        l.append((x))
        x=addTwoStrings(x,x[::-1])#add reverse of two strings
        if x == x[::-1]: #Check palindrome
            nonLychrel=l+nonLychrel
            return False
        if (x) in nonLychrel:
            return False

    return True
def isLychrel(x):
    n=0
    while(n<=50):
        n=n+1
        x=addTwoStrings(x,x[::-1])#add reverse of two strings
        if x == x[::-1]: #Check palindrome
            return False
    return True


def first10Klychrel():
    start = time.time()
    count = 0
    for i in range(10000):
        if isLychrel(str(i))==True:
            count=count+1
    end = time.time()
    print(end - start)
    print count
def first10KlychrelHashed():
    start = time.time()
    count = 0
    for i in range(10000):
        if isLychrelHash(str(i))==True:
            count=count+1
    end = time.time()
    print(end - start)
    print count
def first10KlychrelParallelized():
    start = time.time()
    l=[]
    for x in range(1,10001):
        l.append(str(x))
    
    with closing(Pool(processes=5)) as pool:
        res=pool.map(isLychrel, l)
        pool.terminate()
    print res.count(True)
    end = time.time()
    print(end - start)


first10Klychrel()
first10KlychrelParallelized()
first10KlychrelHashed()


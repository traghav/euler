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
def isLychrel(x):
    n=0
    while(n<=50):
        n=n+1
        x=addTwoStrings(x,x[::-1])#add reverse of two strings
        if x == x[::-1]: #Check palindrome
            return False
    return True
def first10Klychrel():
    count = 0
    for i in range(10000):
        if isLychrel(str(i))==True:
            count=count+1
    print count
first10Klychrel()


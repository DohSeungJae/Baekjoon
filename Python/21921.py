import sys
input=sys.stdin.readline

n,x=map(int,input().split())
visitor=list(map(int,input().split()))

value=sum(visitor[:x])

maxValue=value
maxCnt=1

for i in range(x,n):
    value=value-visitor[i-x]+visitor[i]
    if(value>maxValue):
        maxValue=value
        maxCnt=1

    elif value == maxValue:
        maxCnt+=1

if(maxValue==0):
    print("SAD")
else:
    print(maxValue)
    print(maxCnt)
    
    
    

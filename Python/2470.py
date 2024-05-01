import sys
input=sys.stdin.readline

N=int(input())
nList=list(map(int,input().split()))
nList.sort()

start,end=0,N-1
absMin=sys.maxsize
ans=[0,0]

while start<end:
    sumOfTwo=nList[start]+nList[end]
    absSum=abs(sumOfTwo)
    if(absSum<absMin):
        absMin=absSum
        ans=[nList[start],nList[end]]

    if(sumOfTwo<0):
        start+=1
    else:
        end-=1
    
print(*ans)
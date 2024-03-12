import sys
input=sys.stdin.readline

N,S=map(int,input().split())
numList=list(map(int,input().split()))
sumList=[0]
for num in numList:
    sumList.append(sumList[-1]+num)

start=0
end=0
partSum=0
length=sys.maxsize

while(end<N and start<=end):
    partSum=sumList[end+1]-sumList[start]
    if(partSum>=S):
        length=min(length,end-start+1)
        start+=1
    else:
        end+=1

if(length==sys.maxsize):
    print(0)
else:
    print(length)

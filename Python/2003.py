import sys
input=sys.stdin.readline

n,m=map(int,input().split())
numList=list(map(int,input().split()))

start=0
end=1
partSum=0
cnt=0

while(end<=n and start<=end):
    partSum=sum(numList[start:end])
    if partSum==m:
        cnt+=1
        end+=1
    elif partSum<m:
        end+=1
    else:
        start+=1

print(cnt)

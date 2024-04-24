import sys
input=sys.stdin.readline

N,M=map(int,input().split())
ms=list(map(int,input().split()))
cs=list(map(int,input().split()))
for i in range(N):
    ms[i]=[ms[i],cs[i]]
minCost=sys.maxsize

stack=[]
def bt(start:int)->None:
    global minCost
    sumM=0
    sumC=0
    for i in range(len(stack)):
        sumM+=ms[i][0]
        sumC+=ms[i][1]
    if(sumM>=M):
        minCost=min(minCost,sumC)
        return 

    for i in range(start,N):
        if ms[i] not in stack:
            stack.append(ms[i])
            bt(i+1)
            stack.pop()

bt(0)
print(minCost)

        
import sys
input=sys.stdin.readline

N=int(input())
dist=list(map(int,input().split()))
cost=list(map(int,input().split()))

curCost=sys.maxsize
totalCost=0
for i in range(N-1):
    curCost=min(curCost,cost[i])
    totalCost+=curCost*dist[i]

print(totalCost)


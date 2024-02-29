import sys
import heapq
input=sys.stdin.readline

n=int(input())
m=int(input())
INF=sys.maxsize
arr=[[] for _ in range(n+1)]
minCost=[INF for _ in range(n+1)]
whereFrom={}
for _ in range(m):
    u,v,w=map(int,input().split())
    arr[u].append((v,w))

def dijkstra(start:int)->None:
    q=[]
    heapq.heappush(q,(0,start))
    minCost[start]=0
    while q:
        cost,cur=heapq.heappop(q)
        if(cost>minCost[cur]): ###이부분 중요 
            continue 
        for nextNode,nodeCost in arr[cur]:
            cost=minCost[cur]+nodeCost
            if(cost<minCost[nextNode]):
                minCost[nextNode]=cost
                heapq.heappush(q,(cost,nextNode))
                if(nextNode not in whereFrom.keys()):
                    whereFrom[nextNode]=(cur,cost)
                elif(whereFrom[nextNode][1]>cost):
                    whereFrom[nextNode]=(cur,cost)

def printPath(cur:int)->None:
    stack=[]
    while cur!=start:
        stack.append(cur)
        cur=whereFrom[cur][0]
    stack.append(start)
    print(len(stack))
    print(*stack[::-1])

start,end=map(int,input().split())
dijkstra(start)
print(minCost[end])
printPath(end)


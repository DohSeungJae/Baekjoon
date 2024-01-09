import sys
import heapq
input=sys.stdin.readline

N=int(input())

isConnected=[False for _ in range(N)]
nodeList=[]
edgeList=[]

for i in range(N):
    nodeList.append(list(map(int,input().split())))

 
print(nodeList)

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=[]
INF=sys.maxsize
minCost=[INF for _ in range(N+1)]

def bf(start:int)->None:
    minCost[start]=0
    
    for i in range(N):
        for j in range(M):
            cur,next,cost=arr[j]
            if(minCost[cur]!=INF and minCost[next]>minCost[cur]+cost):
                minCost[next]=minCost[cur]+cost
                if(i==N-1):
                    return True
    return False

for _ in range(M):
    A,B,C=map(int,input().split())
    arr.append((A,B,C))

isNegativeCycle=bf(1)
if(isNegativeCycle):
    print(-1)
    exit(0)

for i in range(2,N+1):
    if(minCost[i]==INF):
        print(-1)
    else:
        print(minCost[i])




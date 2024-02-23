import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
# 10**5일떈 Python3에서 RecursionError
# 10**6일떈 Pypy3에서 메모리초과
# printPathStack을 사용하는 경우에 당연히 재귀제한을 설정할 필요가 없음.

visited=[0]*100001
minCost=[0]*100001
vertexFrom={}

N,K=map(int,input().split())
def bfs(v:int)->None:
    q=deque()
    q.append(v)
    visited[v]=1

    while len(q)>0:
        v=q.popleft()
        if(v==K):
            break
        for next in (v-1,v+1,2*v):
            if(next>100000 or next<0):
                continue
            if(visited[next]==0):
                visited[next]=1
                minCost[next]=minCost[v]+1
                q.append(next)
                if(next not in vertexFrom.keys()):
                    vertexFrom[next]=v

def printPath(cur:int)->None:
    if(cur==N):
        print(cur,end=" ")
        return 
    printPath(vertexFrom[cur])
    print(cur,end=" ")

def printPathStack(cur:int)->None:
    stack=[]
    while cur!=N:
        stack.append(cur)
        cur=vertexFrom[cur]
    stack.append(N)
    print(*stack[::-1])

bfs(N)
print(minCost[K])
printPathStack(K)
#printPath(K)

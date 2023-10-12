import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def cycleDfs(i,visited,n_list):
    global cnt

    visited[i]=True
    next=n_list[i]
    cycle.append(i)
    if visited[next]==False:
        cycleDfs(next,visited,n_list)

    elif next in cycle:
        cnt=cnt-len(cycle)+cycle.index(next)
        

t=int(input())
for _ in range(t):
    n=int(input())
    n_list=[0]+list(map(int,input().split()))

    visited=[0]*(n+1)
    cnt=n
    for i in range(1,n+1):
        cycle=[]
        if not visited[i]:
            cycleDfs(i,visited,n_list)
            
    print(cnt)


 
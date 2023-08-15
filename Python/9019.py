import sys
from collections import deque
input=sys.stdin.readline
maxR=10000
visited=[0]*maxR


def d(n):
    return int((n*2)%maxR)
def s(n):
    return int((n-1+maxR)%maxR)
def l(n):
    return (n*10)%maxR +n//1000
def r(n):
    return (n%10)*1000 + n//10


fName_dict={d:"D",s:"S",l:"L",r:"R"}

def bfs(start,end):
    cmd=[""]*maxR
    q=deque()
    q.append(start)

    while q:
        v=q.popleft()

        for f in (d,s,l,r):
            nextV=f(v)
            if(v==0 and f==d):
                continue
            if(cmd[nextV]==""):

                cmd[nextV]=cmd[v]+fName_dict[f] #
                q.append(nextV)

        
    return cmd[end] 


t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(bfs(a,b))




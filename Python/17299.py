import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
res=[-1 for i in range(n)]
stack=[]

f={}
for i in a:
    if i in f.keys():
        f[i]+=1
    else:
        f[i]=1
    
for i in range(n):
    while stack and f[a[stack[-1]]]<f[a[i]]:
        res[stack.pop()]=a[i]

    stack.append(i)
    

print(*res)

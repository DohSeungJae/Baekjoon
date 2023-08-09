import sys
input=sys.stdin.readline

n=int(input())
res=[-1 for i in range(n)]
a=list(map(int,input().split()))
stack=[]

for i in range(n):
    while stack and a[stack[-1]]<a[i]:
        res[stack.pop()]=a[i]

    stack.append(i)
    

print(*res)

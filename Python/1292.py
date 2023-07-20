import sys
input=sys.stdin.readline

l=[0]
for i in range(1,1000+1):
    for _ in range(i):
        l.append(i)

a,b=map(int,input().split())

sum=0
for i in range(a,b+1):
    sum+=l[i]

print(sum)
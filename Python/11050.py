import sys
input=sys.stdin.readline

n,k=map(int,input().split(" "))

res=1
for i in range(k):
    res=res*n
    n-=1

for i in range(k):
    res=res/k
    k-=1

print(int(res))


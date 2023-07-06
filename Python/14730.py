import sys
input=sys.stdin.readline

n=int(input())
res=0

for _ in range(n):
    c,k=map(int,input().split())
    res+=c*k

print(res)


#미분개색기
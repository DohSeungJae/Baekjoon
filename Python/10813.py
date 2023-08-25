import sys
input=sys.stdin.readline

n,m=map(int,input().split())
basket=[i for i in range(1,n+1)]


for _ in range(m):
    i,j=map(int,input().split())
    i-=1
    j-=1
    temp=basket[i]
    basket[i]=basket[j]
    basket[j]=temp

print(*basket)

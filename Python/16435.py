import sys
input=sys.stdin.readline

N,L=map(int,input().split())
h=list(map(int,input().split()))

for i in range(N):
    if(L>=h[i]):
        L+=1

print(L)

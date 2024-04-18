import sys
from bisect import bisect_left, bisect_right
input=sys.stdin.readline

T=int(input())
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))

cumA,cumB=[],[]
for i in range(n):
    for j in range(i+1,n+1):
        cumA.append(sum(A[i:j]))

for i in range(m):
    for j in range(i+1,m+1):
        cumB.append(sum(B[i:j]))
cumA.sort()
cumB.sort()

cnt=0
for i in range(len(cumA)):
    bStd=T-cumA[i]
    cnt+=bisect_right(cumB,bStd)-bisect_left(cumB,bStd)

print(cnt)
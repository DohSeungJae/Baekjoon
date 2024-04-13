import sys
input=sys.stdin.readline

T=int(input())
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))

cumA=[0]
for a in A:
    cumA.append(cumA[-1]+a)

cumB=[0]
for b in B:
    cumB.append(cumB[-1]+b)

 
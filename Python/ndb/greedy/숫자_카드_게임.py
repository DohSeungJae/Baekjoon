import sys
input=sys.stdin.readline

N,M=map(int,input().split())

max_among_mins=0
for _ in range(N):
    line=list(map(int,input().split()))
    max_among_mins=max(max_among_mins, min(line))

print(max_among_mins)

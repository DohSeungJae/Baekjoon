import sys
input=sys.stdin.readline

summary=0
n=int(input())
for _ in range(n):
    summary+=int(input())

print(summary)

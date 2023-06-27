import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
d=deque([i for i in range(1,n+1)])

while(len(d)>1):
    d.popleft()
    d.append(d.popleft())

print(d.popleft())
import sys
from collections import deque
input=sys.stdin.readline

d=deque()
n=int(input())
for _ in range(n):
    cmd=input().strip().split()

    if cmd[0]=="push":
        d.append(cmd[1])

    elif cmd[0]=="pop":
        if(len(d)>0):
            print(d.popleft())
        else:
            print(-1)
        
    elif cmd[0]=="size":
        print(len(d))

    elif cmd[0]=="empty":
        print(int(not bool(len(d))))

    elif cmd[0]=="front":
        if len(d)>0:
            print(d[0])
        else:
            print(-1)
    else:
        if len(d)>0:

            print(d[-1])
        else:
            print(-1)

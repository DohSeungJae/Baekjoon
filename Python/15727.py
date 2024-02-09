import sys
input=sys.stdin.readline

L=int(input())

t=L/5
if(t==int(t)):
    print(int(t))
else:
    print(int(t)+1)
import sys
input=sys.stdin.readline

L=int(input())

t=L/4
if(t==int(t)):
    print(t)
else:
    print(int(t)+1)
    
    
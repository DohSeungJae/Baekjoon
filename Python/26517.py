import sys
input=sys.stdin.readline

k=int(input())
a,b,c,d=map(int,input().split())

v=a*k+b
if(v!=c*k+d):
    print("No")
    exit(0)
else:
    print("Yes",v)


#연속인가?

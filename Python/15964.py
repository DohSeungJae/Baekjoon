import sys
input=sys.stdin.readline

def cal(a:int,b:int)->int:
    return (a+b)*(a-b)

a,b=map(int,input().split())
print(cal(a,b))

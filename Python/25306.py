import sys
input=sys.stdin.readline

def xor1To(n:int)->int:
    if(n%4==0):
        return n
    elif(n%4==3):
        return 0
    elif(n%4==2):
        return n+1
    else:
        return 1

A,B=map(int,input().split())
print(xor1To(A-1)^xor1To(B))
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
stack=[]

def backTracking(start):
    if len(stack)==m:
        print(*stack)
        return 
     
    for i in range(start,n+1):
            if(i>=start):
                stack.append(i)
                backTracking(i)
                stack.pop()

backTracking(1)

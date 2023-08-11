import sys
input=sys.stdin.readline

n,m=map(int,input().split())
stack=[]

def backTracking():
    if len(stack)==m:
        b=1
        for i in range(m-1):
           if(not stack[i]<stack[i+1]):
               b=0

        if b: print(*stack)
        return 
    
    for i in range(1,n+1):
        if i not in stack:
            stack.append(i)
            backTracking()
            stack.pop()

backTracking()

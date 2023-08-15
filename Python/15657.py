import sys
input=sys.stdin.readline

n,m=map(int,input().split())
n_list=list(map(int,input().split()))
n_list.sort()
stack=[]

def backTracking(startIdx):
    if(len(stack)==m):
        print(*stack)
        return 
    
    
    for i in range(startIdx,n):
        if(i>=startIdx):
            stack.append(n_list[i])
            backTracking(i)
            stack.pop()

backTracking(0)

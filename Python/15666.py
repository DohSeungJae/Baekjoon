import sys
input=sys.stdin.readline

n,m=map(int,input().split())
n_list=list(map(int,input().split()))
n_list.sort()

stackVisited=set()
stack=[]

def backTracking(start):
    if len(stack)==m:
        if tuple(stack) not in stackVisited:
            stackVisited.add(tuple(stack))
            print(*stack)

        return 
     
    for i in range(start,n):
        
        stack.append(n_list[i])
        backTracking(i)
        stack.pop()


backTracking(0)

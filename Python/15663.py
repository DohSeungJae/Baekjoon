import sys
input=sys.stdin.readline

n,m=map(int,input().split())
n_list=list(map(int,input().split()))
n_list.sort()

stackVisited=set()
stack=[]
nVisited={}
for i in range(n):
    nVisited[i]=0

def backTracking():
    if len(stack)==m:
        if tuple(stack) not in stackVisited:
            stackVisited.add(tuple(stack))
            print(*stack)

        return 
     
    for i in range(n):
        if nVisited[i]==0:
            nVisited[i]=1
            stack.append(n_list[i])
            backTracking()
            stack.pop()
            nVisited[i]=0

backTracking()

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
n_list=list(map(int,input().split()))
n_list.sort()
stack=[]
visitDict={}
for i in n_list:
    visitDict[i]=0

def backTracking():
    if(len(stack)==m):
        print(*stack)
        return 
    
    for i in range(n):
        num=n_list[i]
        if visitDict[num]==0:
            visitDict[num]=1
            stack.append(num)
            backTracking()
            stack.pop()
            visitDict[num]=0

backTracking()
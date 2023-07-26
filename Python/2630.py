import sys
input=sys.stdin.readline

n=int(input())
graph=[]

cnt=[0,0]
for _ in range(n): graph.append(list(map(int,input().split())))
xs=[0,0,1,1]
ys=[0,1,0,1]

def dividing(graph,n,cnt):
    std=graph[0][0]

    if(not isEqual(std,graph,n)):
        for i in range(4):
            dgraph=newGraph(graph,n//2,xs[i],ys[i])
            cnt=dividing(dgraph,n//2,cnt)            
    else:
        cnt[std]+=1
    return cnt

def newGraph(graph,n,x_idx,y_idx):

    new=[[0]*n for i in range(n)]
    for y in range(n):
        for x in range(n):
            new[y][x]=graph[y+(y_idx*n)][x+(x_idx*n)]
            
    return new

def isEqual(std,graph,n):
    for y in range(n):
        for x in range(n):
            if(std!=graph[y][x]):
                return False     
    return True

cnt=dividing(graph,n,cnt)

print(cnt[0])
print(cnt[1])



            
    
    




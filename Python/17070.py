import sys
input=sys.stdin.readline

cord1=[0,1]
def dfs(cord1:list,curStatus:int)->None: 
    global cnt
    if(cord1==[N-1,N-1]):
        cnt+=1
        return 
    for nextStatus in range(3):
        if(nextStatus==0):
            nextX=cord1[1]+1
            nextY=cord1[0]
            if(curStatus==2):
                continue
            elif(nextX==N):
                continue
            elif(graph[nextY][nextX]==1):
                continue

        elif(nextStatus==1):
            nextX=cord1[1]+1
            nextY=cord1[0]+1
            if(nextX==N or nextY==N):
                continue
            elif(graph[nextY][nextX]==1 or \
               graph[nextY-1][nextX]==1 or graph[nextY][nextX-1]==1):
                continue

        else:
            nextX=cord1[1]
            nextY=cord1[0]+1
            if(curStatus==0):
                continue
            elif(nextY==N):
                continue
            elif(graph[nextY][nextX]==1):
                continue
        
        dfs([nextY,nextX],nextStatus)

N=int(input())

status=0
graph=[]
cnt=0

for _ in range(N):
    line=list(map(int,input().split()))
    graph.append(line)

if(graph[N-1][N-1]==1):
    print(0)
    exit(0)

dfs(cord1,status)
print(cnt)

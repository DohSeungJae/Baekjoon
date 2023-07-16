import sys
import queue
input=sys.stdin.readline

def bfs(matrix,xy):
    visited=[]
    visited.append(xy)

    q=queue.Queue()
    q.put(xy)

    while not q.empty():
        xy=q.get()
        x=xy[0]
        y=xy[1]

        temp=[]
        temp.append([x,y+1])
        temp.append([x,y-1])
        temp.append([x+1,y])
        temp.append([x-1,y])

        for xy in temp:
            x=xy[0]
            y=xy[1]
            if(x>=0 and y>=0 and x<m and y<n):
                if(matrix[y][x]==1 and [x,y] not in visited):
                    q.put([x,y])
                    visited.append([x,y])
                
    return visited

t=int(input())

for _ in range(t):
    m,n,k=map(int,input().split())
    matrix=[[0]*(m) for i in range(n)]

    cord=[]
    for __ in range(k):
        x,y=map(int,input().split())
        cord.append([x,y])
        matrix[y][x]=1

    cnt=0
    visit=[]
    for xy in cord:
        if xy not in visit:
            cnt+=1
            visit+=bfs(matrix,xy)
            print(visit)



    print(cnt)


    

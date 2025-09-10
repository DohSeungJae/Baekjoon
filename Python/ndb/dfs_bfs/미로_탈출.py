from collections import deque
import sys
input=sys.stdin.readline

dy=[1,-1,0,0]
dx=[0,0,1,-1]

N,M=map(int,input().split())
board=[]
for _ in range(N):
    board.append(list(map(int,input().strip())))

dist=[[0 for _ in range(M)] for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]

def bfs(start_y,start_x):
    start=[start_y,start_x]
    q=deque([start])
    dist[start_y][start_x]=1

    while q:
        y,x=q.popleft()
        visited[y][x]=1

        for i in range(4):
            next_y=y+dy[i]
            next_x=x+dx[i]

            if(next_y>=N or next_y<0 or next_x>=M or next_x<0):
                continue
            if(visited[next_y][next_x]==1):
                continue
            if(board[next_y][next_x]==0):
                continue
            dist[next_y][next_x]=dist[y][x]+1
            q.append([next_y,next_x])

    print(dist[N-1][M-1])

bfs(0,0)     

    
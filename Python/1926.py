import sys
import queue
from collections import deque
input=sys.stdin.readline

aroundX=[0,0,1,-1]
aroundY=[1,-1,0,0]

def bfs(matrix,start):
    cnt=1
    matrix[start[1]][start[0]]=0

    q=deque()
    q.append(start)

    while q:
        xy=q.popleft()
        x=xy[0]
        y=xy[1]

        for i in range(4):
            nearX=x-aroundX[i]
            nearY=y-aroundY[i]

            if((0<=nearY<n) and (0<=nearX<m)):
                next=[nearX,nearY]
                if(matrix[nearY][nearX]==1):
                    matrix[nearY][nearX]=0
                    q.append(next)
                    cnt+=1
    return cnt


n,m=map(int,input().split())

matrix=[]

for _ in range(n):
    matrix.append(list(map(int,input().split())))

paint=[]

max_len=0
cnt_pic=0
for y in range(n):
    for x in range(m):
        if(matrix[y][x]==1):
            paint.append(bfs(matrix,[x,y]))


if(len(paint))==0:
    print(0)
    print(0)
else:
    print(len(paint))
    print(max(paint))


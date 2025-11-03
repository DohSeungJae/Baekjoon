from collections import deque

def rotate_left(d):
    return 3 if(d==0) else (d-1)

def rotate_right(d):
    return (d+1)%4

def is_end(ny,nx):
    if(ny<1 or nx<1 or nx>=(n+1) or ny>=(n+1)):
        return True
    if(board[ny][nx]==1):
        return True
    return False

n=int(input())
board=[[0]*(n+1) for _ in range(n+1)]

k=int(input())
for _ in range(k):
    col,row=map(int,input().split())
    board[col][row]=2 #사과는 2로 표시

l=int(input())
rotate_when=[0]*(10000+1)
for _ in range(l):
    time,d=map(str,input().split())
    rotate_when[int(time)]=d

# 0: 우 1: 하 2: 좌 3:상 // 시계방향으로 회전하면 숫자 높아짐
dy=[0,1,0,-1]
dx=[1,0,-1,0]

d=0 #direction
y,x=1,1
board[y][x]=1 #뱀은 1로 표시
snake=deque([[y,x]])
for time in range(1,10001):
    ny,nx=y+dy[d],x+dx[d]
    if(is_end(ny,nx)):
        print(time)
        break

    snake.append([ny,nx])
    if(board[ny][nx]!=2):
        ly,lx=snake.popleft()
        board[ly][lx]=0
    board[ny][nx]=1

    rotate=rotate_when[time]
    if(rotate=="L"):
        d=rotate_left(d)
    elif(rotate=="D"):
        d=rotate_right(d)

    y,x=ny,nx
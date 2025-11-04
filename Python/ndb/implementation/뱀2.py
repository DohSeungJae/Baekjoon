from collections import deque
MAXTIME=10000

#기본 방향이 우측이므로
#우:0, 하:1, 좌:2, 상:3 으로 설정
#오른쪽으로 회전할 수록 숫자 높아짐
dy=[0,1,0,-1]
dx=[1,0,-1,0]
def rotate_right(d):
    return (d+1)%4 #방향이 4개이므로 %4

def rotate_left(d):
    return 3 if(d==0) else (d-1)

def can_go(ny,nx):
    if(ny<1 or nx<1 or ny>n or nx>n): #범위 설정에 주의
        return False
    if(board[ny][nx]==1):
        return False
    return True

n=int(input())
board=[[0]*(n+1) for _ in range(n+1)]

k=int(input())
for _ in range(k):
    col,row=map(int,input().split())
    board[col][row]=2 #사과는 2로 표시

l=int(input())
rotate_when=[0]*(MAXTIME+1)
for _ in range(l):
    x,c=map(str,input().split())
    rotate_when[int(x)]=c

d=0
y,x=1,1
snake=deque([(y,x)])
board[y][x]=1
for time in range(1,MAXTIME+1): 
    ny,nx=y+dy[d],x+dx[d]

    if(not can_go(ny,nx)):
        print(time)
        break
    
    snake.append((ny,nx))
    if(board[ny][nx]!=2):
        ly,lx=snake.popleft()
        board[ly][lx]=0
    board[ny][nx]=1

    if(rotate_when[time]=="L"):
        d=rotate_left(d)
    elif(rotate_when[time]=="D"):
        d=rotate_right(d)
    
    y,x=ny,nx






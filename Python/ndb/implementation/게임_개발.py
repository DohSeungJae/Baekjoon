import sys
input=sys.stdin.readline

#y,x 순서
directions=[[-1,0],[0,1],[1,0],[0,-1]]

def turn_left():
    global d
    if(d==0):
        d=3
        return 
    d-=1

N,M=map(int,input().split())
y,x,d=map(int,input().split())
board=[]
visited=[[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(int,input().split())))

turn_cnt=0
visited_cnt=1
visited[y][x]=1
while 1:
    if(board[y][x]==1):
        break
    if(turn_cnt==4):
        dy,dx=directions[d]
        y=y-dy
        x=x-dx
        continue

    turn_left()
    dy,dx=directions[d]
    next_y=y+dy
    next_x=x+dx
    if(visited[next_y][next_x]==1 or board[next_y][next_x]==1):
        turn_cnt+=1
        continue

    turn_cnt=0
    visited[next_y][next_x]=1
    visited_cnt+=1
    y=next_y
    x=next_x

print(visited_cnt)



        


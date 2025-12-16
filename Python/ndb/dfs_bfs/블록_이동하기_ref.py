from collections import deque

def get_next_pos(board,pos): #현재 위치에서 순회/회전 가능한 모든 경우를 반환
    next_pos=[]
    pos=list(pos)
    p1_y,p1_x,p2_y,p2_x=pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(4): #이동 가능한지
        p1_ny,p1_nx,p2_ny,p2_nx=p1_y+dy[i],p1_x+dx[i],p2_y+dy[i],p2_x+dx[i]
        if(board[p1_ny][p1_nx]==0 and board[p2_ny][p2_nx]==0):
            npos={(p1_ny,p1_nx),(p2_ny,p2_nx)}
            next_pos.append(npos)
    
    if(p1_y==p2_y): #가로 상태에서 회전 가능한지
        for i in [-1,1]: #위로 회전 / 아래로 회전  
            if(board[p1_y+i][p1_x]==0 and board[p2_y+i][p2_x]==0): #축 상관없이 회전 방향으로 앞 1칸은 모두 0이여야함
                npos1={(p1_y,p1_x),(p2_y+i,p1_x)} #p1을 축으로 회전하는 경우
                npos2={(p1_y+i,p2_x),(p2_y,p2_x)} #p2를 축으로 회전하는 경우 
                next_pos.append(npos1)
                next_pos.append(npos2)
                #위 조건만 만족한다면 p1축 회전, p2축 회전이 모두 가능하고
                #그렇지 않다면 둘 다 불가능함
                
    
    if(p1_x==p2_x): #세로 상태에서 회전 가능한지
        for i in [-1,1]:
            if(board[p1_y][p1_x+i]==0 and board[p2_y][p2_x+i]==0):
                npos1={(p1_y,p1_x),(p1_y,p2_x+i)}
                npos2={(p2_y,p1_x+i),(p2_y,p2_x)}
                next_pos.append(npos1)
                next_pos.append(npos2)
    
    return next_pos

def solution(board):
    n=len(board)
    new_board=[[1]*(n+2) for _ in range(n+2)]
    for y in range(n):
        for x in range(n):
            new_board[y+1][x+1]=board[y][x]
    
    q=deque()
    visited=[]
    pos={(1,1),(1,2)} #(y,x)
    q.append((pos,0)) #(position, cost)
    visited.append(pos)
    
    while q:
        pos,cost=q.popleft()
        if((n,n) in pos):
            return cost
        
        for next_pos in get_next_pos(new_board,pos): #현재 위치에서 가능한 이동/회전을 모두 순회
            if(next_pos not in visited):
                visited.append(next_pos)
                q.append((next_pos,cost+1))

    return 0
            
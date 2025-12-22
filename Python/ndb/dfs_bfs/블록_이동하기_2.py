from collections import deque

def get_next_pos(board, pos):
    next_pos=[]
    pos=list(pos)
    
    p1_y,p1_x,p2_y,p2_x=pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(4):
        p1_ny,p1_nx,p2_ny,p2_nx=p1_y+dy[i],p1_x+dx[i],p2_y+dy[i],p2_x+dx[i]
        if(board[p1_ny][p1_nx]==0 and board[p2_ny][p2_nx]==0):
            npos={(p1_ny,p1_nx),(p2_ny,p2_nx)}
            next_pos.append(npos)
    
    if(p1_y==p2_y): #가로 상태
        for i in [-1,1]:
            if(board[p1_y+i][p1_x]==0 and board[p2_y+i][p2_x]==0):
                npos1={(p1_y+i,p2_x),(p2_y,p2_x)}
                npos2={(p1_y,p1_x),(p2_y+i,p1_x)}
                next_pos.append(npos1)
                next_pos.append(npos2)
        
    if(p1_x==p2_x): #세로 상태
        for i in [-1,1]:
            if(board[p1_y][p1_x+i]==0 and board[p2_y][p2_x+i]==0):
                npos1={(p2_y,p1_x+i),(p2_y,p2_x)}
                npos2={(p1_y,p1_x),(p1_y,p2_x+i)}
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
    pos={(1,1),(1,2)} #{(y1,x1),(y2,x2)}
    q.append((pos,0))
    visited.append(pos)
    while q:
        pos,cost=q.popleft()
        if((n,n) in pos):
            return cost
        
        for next_pos in get_next_pos(new_board,pos):
            if(next_pos not in visited):
                q.append((next_pos,cost+1))
                visited.append(next_pos)
            
            
    return 0
import sys
input=sys.stdin.readline

def rotate(stk):
    r,c=len(stk),len(stk[0])
    turned=[[0 for _ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            #turned[i][j]=stk[j][(r-1)-i] #OOI
            turned[j][(r-1)-i]=stk[i][j]
    return turned

def is_possible(y,x,stk):
    r,c=len(stk),len(stk[0])
    for i in range(r):
        for j in range(c):
            if((y+i)>=n or (x+j)>=m):  ##OOI
                return False
            if(board[y+i][x+j]==1 and stk[i][j]==1):
                return False
    
    return True

def attach(y,x,stk):
    r,c=len(stk),len(stk[0])
    for i in range(r):
        for j in range(c):
            if(board[y+i][x+j]==0 and stk[i][j]==1):
                board[y+i][x+j]=1

n,m,k=map(int,input().split())
board=[[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    stk=[]
    r,c,=map(int,input().split())
    for _ in range(r):
        row=list(map(int,input().split()))
        stk.append(row)

    for i in range(4):
        if(stk==[]): break
        if(i!=0): stk=rotate(stk)
        for y in range(n):
            for x in range(m):
                if(stk==[]): break
                possible=is_possible(y,x,stk)
                if(possible):
                    attach(y,x,stk)
                    stk=[]
                               
cnt=0
for row in board:
    for n in row:
        cnt+=n

print(cnt)
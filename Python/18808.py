import sys
input=sys.stdin.readline

def turn_clockwise(stk): #시계 방향으로 회전
    h=len(stk)
    w=len(stk[0])
    
    stk_turn=[[0 for _ in range(h)] for _ in range(w)]
    for y in range(h):
        for x in range(w):
            stk_turn[x][(h-1)-y]=stk[y][x]

    return stk_turn

def OOI(y,x): #Out of Index
    #if(y>0 or x<0 or x>=m or y>=n):
        #return True
    if(x>=m or y>=n): #어차피 좌측상단에서 시작하기 때문에 
        #좌표가 -인 경우는 고려하지 않아도됨
        return True
    return False

def is_possible(y,x,stk):
    #스티커를 board에 붙일 수 있는지 확인
    #y,x는 스티커를 붙일 board 상의 좌표
    #스티커의 좌측상단이 y,x에 위치하게됨.

    #스티커의 모든 부분을 board에 붙일 수 있는지 체크
    #범위 밖이거나(OOI) 이미 다른 스티커가 붙여져 있는 경우(board[][]==1)에는 붙일 수 없음.
    h=len(stk)
    w=len(stk[0])
    for sy in range(h): #sticker y
        for sx in range(w): #sticker x
            if(OOI(y+sy,x+sx)):
                return False
            if(board[y+sy][x+sx]==1 and stk[sy][sx]==1):
                return False
     
    return True

def stick(y,x,stk): #스티커 붙이기 
    h=len(stk)
    w=len(stk[0])
    for sy in range(h):
        for sx in range(w):
            if(board[y+sy][x+sx]==0 and stk[sy][sx]==1):
                board[y+sy][x+sx]=1    


n,m,k=map(int,input().split())
stks=[] #stickers
board=[[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    stk=[] #sticker
    h,w=map(int,input().split())
    for _ in range(h):
        stk.append(list(map(int,input().split())))
    stks.append(stk)

for stk in stks:
    for i in range(4):
        if(stk==[]):continue
        if(i!=0): stk=turn_clockwise(stk)
        for y in range(n):
            for x in range(m):
                if(stk==[]):continue
                possible=is_possible(y,x,stk)
                if(possible):
                    stick(y,x,stk)
                    stk=[]
                    break
                
cnt=0
for y in range(n):
    for x in range(m):
        if(board[y][x]==1):
            cnt+=1

print(cnt)

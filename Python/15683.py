import sys

#상 우 하 좌 (시계방향) 
around_y=[-1,0,1,0]
around_x=[0,1,0,-1]

def OOI(y,x): #Out of Index
    if(y<0 or y>=n or x<0 or x>=m):
        return True
    return False

def upd(y,x,d):
    d=d%4
    while 1:
        y,x=y+around_y[d],x+around_x[d]
        if(OOI(y,x)):
            break
        if(board2[y][x]==6):
            break
        if(board2[y][x]!=0):
            continue #이 코드 블럭은 정답에 영향이 없음
        board2[y][x]=7

def init_board2():
    for y in range(n):
        for x in range(m):
            board2[y][x]=board1[y][x]

def get_blind_spot():
    blind=0
    for y in range(n):
        for x in range(m):
            if(board2[y][x]==0):
                blind+=1
    
    return blind

n,m=map(int,input().split())
board1=[] #원본
board2=[[0 for _ in range(m)] for _ in range(n)] #계산 시 사용 및 초기화
cctv=[] #(y,x,model) #model은 cctv 종류
for y in range(n):
    line=list(map(int,input().split()))
    for x in range(m):
        if(1<=line[x]<=5):
            cctv.append((y,x,line[x])) #cctv의 위치와 종류 저장
    board1.append(line)

min_blind=sys.maxsize
for case in range(4**(len(cctv))): #cctv 방향이 최대 4개이기 때문
    init_board2()
    brute=case
    for (y,x,model) in cctv:

        #4진수에서 각 자리수 구하기
        d=brute%4
        brute=brute//4

        if(model==1):
            upd(y,x,d)
        elif(model==2):
            upd(y,x,d)
            upd(y,x,d+2)
        elif(model==3):
            upd(y,x,d)
            upd(y,x,d+1)
        elif(model==4):
            upd(y,x,d)
            upd(y,x,d+1)
            upd(y,x,d+2)
        else: #model==5
            upd(y,x,d)
            upd(y,x,d+1)
            upd(y,x,d+2)
            upd(y,x,d+3)

    blind=get_blind_spot()
    min_blind=min(min_blind,blind)

print(min_blind)

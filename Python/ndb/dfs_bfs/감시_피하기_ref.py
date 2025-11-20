from itertools import combinations

n=int(input())
board=[]
blank=[] #[[x,y] ...]
tch=[] #[[x,y] ...], teacher

def is_possible():
    for x,y in tch:
        if(teacher_got_student(x,y)):
            return False
    return True

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def teacher_got_student(x,y):
    for i in range(4):
        nx,ny=x,y
        while 1:
            nx,ny=nx+dx[i],ny+dy[i]
            #nx,ny=x+dx[i],y+dy[i] <- 오답 판정 
            if(nx<0 or nx>=n or ny<0 or ny>=n):
                break
            if(board[ny][nx]=="O"):
                break
            #x,y=nx,ny <- 오답 판정 <- 이 x,y는 for문 다음 step에서 사용되어야 하기 때문에 이 값을 변경하면 안됨.
            if(board[ny][nx]=="S"):
                return True
            
    return False

for y in range(n):
    line=list(map(str,input().split()))
    for x in range(n):
        if(line[x]=='X'):
            blank.append([x,y])
        elif(line[x]=='T'):
            tch.append([x,y])
    board.append(line)


possible=False
for build in combinations(blank,3):
    for i in range(3):
        x,y=build[i]
        board[y][x]="O"
    
    if(is_possible()):
        print("YES")
        possible=True
        break

    for i in range(3):
        x,y=build[i]
        board[y][x]="X"

if(not possible):
    print("NO")


from itertools import combinations

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def is_possible():
    for x,y in tch:
        for i in range(4):
            tx,ty=x,y #좌표 계산은 tx,ty로
            while 1:
                tx,ty=tx+dx[i],ty+dy[i]
                if(tx<0 or tx>=n or ty<0 or ty>=n):
                    break
                elif(board[ty][tx]=="O"):
                    break
                elif(board[ty][tx]=="S"):
                    return False
    return True        

n=int(input())
board=[]
tch=[] #[[x,y] ...]
blk=[] #[[x,y] ...]
for y in range(n):
    line=list(map(str,input().split()))
    for x in range(n):
        if(line[x]=="T"):
            tch.append([x,y])
        elif(line[x]=="X"):
            blk.append([x,y])
    board.append(line)

possible=False
for objs in combinations(blk,3):
    for obj in objs:
        x,y=obj
        board[y][x]="O"

    possible=is_possible()
    if(possible):
        break

    for obj in objs:
        x,y=obj
        board[y][x]="X"

if(possible):
    print("YES")
else:
    print("NO")
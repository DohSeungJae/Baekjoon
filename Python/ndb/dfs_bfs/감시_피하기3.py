from itertools import combinations
#combinations Vs. permutations
'''
combinations(조합)는 순서를 고려하지 않기 때문에
동일한 원소 집합은 한 번만 결과에 포함됨
예를 들어 (A,B)와 (B,A)는 순서는 다르지만 같은 원소 집합이므로
같은 것으로 취급되어 하나만 생성됨
'''

'''
permutations(순열)는 순서를 고려하기 때문에
동일한 원소 집합이더라도 순서가 다르면 다른 것으로 취급함
예를 들어 (A,B)와 (B,A)는 같은 원소 집합이지만 순서가 다르기 때문에
둘 다 생성됨
'''

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def is_possible():
    for x,y in tch:
        #여기서 좌표 초기화 하면 안됨
        for i in range(4):
            tx,ty=x,y #좌표 초기화는 여기서 해야함
            #방향(i)을 바꿀 때 마다 원래 위치로 돌아와야 하기 때문에
            while 1:
                tx,ty=tx+dx[i],ty+dy[i]
                if(tx<0 or tx>=n or ty<0 or ty>=n):
                    break
                if(board[ty][tx]=="O"):
                    break
                if(board[ty][tx]=="S"):
                    return False
    return True

n=int(input())
board=[]
tch=[] #[ [x,y] ...] ,teacher 
blk=[] #[ [x,y] ...] ,blank

for y in range(n):
    line=list(map(str,input().split()))
    for x in range(n):
        if(line[x]=="T"):
            tch.append([x,y])
        elif(line[x]=="X"):
            blk.append([x,y])
    board.append(line)


possible=False
for build in combinations(blk,3):
    for x,y in build:
        board[y][x]="O"
    
    possible=is_possible()
    if(possible): break

    for x,y in build:
        board[y][x]="X"


if(possible):
    print("YES")
else:
    print("NO")


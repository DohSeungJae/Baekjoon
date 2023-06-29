
import sys
input=sys.stdin.readline

n,m=map(int,input().split(" "))
board=[]
cnts=[]

for _ in range(n):
    
    board.append(list(input().strip()))

for y in range(n-8+1):
    for x in range(m-8+1):
        cnt_w=0
        cnt_b=0

        for i in range(y,y+8):
            for j in range(x,x+8):
                if(i+j)%2==0:
                    if(board[i][j]!="W"):
                        cnt_w+=1
                    else:
                        cnt_b+=1
                else:
                    if(board[i][j]!="W"):
                        cnt_b+=1
                    else:
                        cnt_w+=1


        cnts.append(min(cnt_w,cnt_b))


print(min(cnts))



N=int(input())
board=[[" " for _ in range(N)] for _ in range(N)]

def draw(y:int,x:int)->None:
    for i in range(3):
        board[y+0][x+i]="*"
        board[y+2][x+i]="*"
    for i in range(0,3,2):
        board[y+1][x+i]="*"

def recursion(n:int,y:int,x:int):
    if(n==3):
        draw(y,x)
    else:
        nextN=n//3
        for i in range(3):
            recursion(nextN,y,x+nextN*i)
            recursion(nextN,y+2*nextN,x+nextN*i)
        for i in range(0,3,2):
            recursion(nextN,y+1*nextN,x+nextN*i)

recursion(N,0,0)
for line in board:
    for i in line:
        print(i,end="")
    print()
    

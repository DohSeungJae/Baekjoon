N=int(input())
board=[[' ' for _ in range(2*N-1)] for _ in range(N)]

def draw(y:int,x:int)->None:
    board[y][x]="*"
    for i in range(-1,2,2):
        board[1+y][i+x]="*"
    for i in range(-2,3):
        board[2+y][i+x]="*"

def recursion(n:int,y:int,x:int)->None:
    if(n==3):
        draw(y,x)
    else:
        nextN=n//2
        recursion(nextN,y,x)
        recursion(nextN,y+nextN,x-nextN)
        recursion(nextN,y+nextN,x+nextN)

recursion(N,0,N-1)
for line in board:
    for i in line:
        print(i,end="")
    print()
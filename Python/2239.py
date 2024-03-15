import sys
input=sys.stdin.readline

board=[]
zeroes=[]
isDefinedRow=[{i+1:False for i in range(9)} for _ in range(9)] 
isDefinedColumn=[{i+1:False for i in range(9)} for _ in range(9)]
isDefinedBox=[{i+1:False for i in range(9)} for _ in range(9)]  

for y in range(9):
    line=input().strip()
    temp=[int(i) for i in line]
    for x in range(len(temp)):
        integer=temp[x]
        if(integer==0):
            zeroes.append([y,x])
        else:
            isDefinedRow[x][integer]=True
            isDefinedColumn[y][integer]=True
            idxOfBox=(x//3)+(y//3)*3
            isDefinedBox[idxOfBox][integer]=True
    
    board.append(temp)

stack=[]
def backTracking(start:int)->None:
    if(start<=25):
        print(start)

        for line in board:
            for i in line:
                print(i,end="")
            print()
        print()


    if(len(stack)==len(zeroes)):
        for line in board:
            for i in line:
                print(i,end="")
            print()
        print()
        return 
    
    for i in range(start,len(zeroes)):
        y,x=zeroes[i][0],zeroes[i][1]
        idxOfBox=(x//3)+(y//3)*3
        if([y,x] in stack):
            continue
        adopted=0
        for integer in range(1,9+1):
            if(isDefinedRow[x][integer]):
                continue
            if(isDefinedColumn[y][integer]):
                continue
            if(isDefinedBox[idxOfBox][integer]):
                continue
            adopted=integer

            stack.append([y,x])
            isDefinedRow[x][adopted]=True
            isDefinedColumn[y][adopted]=True
            isDefinedBox[idxOfBox][adopted]=True
            board[y][x]=adopted
            backTracking(i+1)
            stack.pop()
            isDefinedRow[x][adopted]=False
            isDefinedColumn[y][adopted]=False
            isDefinedBox[idxOfBox][adopted]=False
            board[y][x]=0
        if(adopted==0):
            return 

backTracking(0)


    
    


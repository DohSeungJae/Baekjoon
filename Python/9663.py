import sys
input=sys.stdin.readline

N=int(input())
if(N==1 or N==2 or N==3):
    print(int(not bool(N-1)))
    exit(0)
board=[0]*N

br=0
def bt(curCnt,n:int)->None:
    global br 
    if(n==curCnt):
        br+=1
        return
    
    for i in range(n):
        isSet=1
        for j in range(curCnt):
            if(board[j]==i or abs(curCnt-j)==abs(i-board[j])):
                isSet=0
                break
        if(isSet):
            board[curCnt]=i
            bt(curCnt+1,n)


bt(0,N)
print(br)

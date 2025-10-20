
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)] #원본
board2=[[0 for _ in range(n)] for _ in range(n)] #계산 시 사용

def init_board2():
    for y in range(n):
        for x in range(n):
            board2[y][x]=board[y][x] 



# 방향 ; 0:상, 1:하, 2:좌, 3:우
def move_right(): #d==3일 때, 
    for row in range(n): #row 내에서 움직이므로 row 순서는 상관 없음
        for i in range(n-1,-1,-1): #인덱스가 높은 순서부터 column 검사
            if(board2[row][i]==0): #빈칸 -> 제외
                continue
            col=i
            while 1:
                if(col==n-1): #이미 도착지점에 있는 숫자는 이동시키지 않음
                    break
                if(board2[row][col+1]==0): #가려고 하는 곳이 빈칸이라면 -> 갈 수 있음
                    board2[row][col+1]=board2[row][col] #1칸 앞으로
                    board2[row][col]=0 #원래 칸은 비워두기
                elif(board2[row][col+1]==board2[row][col] and board2[row][col+1]>0): #만약 앞 칸이 빈칸이 아니고(elif), 자신과 같고, 이전에 더해지지 않았다면
                    board2[row][col+1]+=board2[row][col] #두 수를 더하고
                    board2[row][col]=0 #원래 칸은 비워두고
                    board2[row][col+1]*=(-1) #한 줄 이동이 끝나면 (-)를 (+)로 바꿔줘야함
                col+=1 
                if(col<=0): #이 부분 수정 필요
                    break
                
        for col in range(n):
            if(board2[row][col]>0):
                continue
            board2[row][col]*=(-1)
        
def move_left(): #d==2일 때
    for row in range(n): #row 내에서 움직이므로 row 순서는 상관없음
        for i in range(n): #move_right와 다르게 왼쪽 칸(낮은 인덱스)부터 움직임
            if(board2[row][i]==0): #선택한 칸이 빈칸이라면 -> 제외
                continue
            col=i 
            while 1:
                if(col==0 or col==n): #이미 도착 지점(가장 왼쪽)에 있는 숫자는 이동하지 않음 // n인 경우는 이미 다 탐색한 경우, 이 경우에도 종료
                    break
                if(board2[row][col-1]==0): #현재 바로 왼쪽 칸이 빈칸이라면 -> 갈 수 있음
                    board2[row][col-1]=board2[row][col] #1칸 왼쪽으로
                    board2[row][col]=0 #원래 칸은 빈 칸
                elif(board2[row][col-1]==board2[row][col] and board2[row][col-1]>0): #만약 왼쪽 칸이 빈칸이 아니고(elif에 의해), 자신과 같으며, 이전에 더해지지 않았다면
                    board2[row][col-1]+=board2[row][col] #두 수를 더하고
                    board2[row][col]=0 #원래 칸은 빈 칸이고
                    board2[row][col-1]*=(-1) #더해진 칸은 (-)로 정함, 한 줄 이동이 끝나면 (+)로 바꿔줘야함.
                col-=1 #-로 변경 

        for col in range(n):
            if(board2[row][col]>0):
                continue
            board2[row][col]*=(-1)


def move_up(): #d==0
    for col in range(n): #같은 column 내에서 움직이므로 column 순서는 상관 없음
        for i in range(n): #낮은 인덱스부터 움직임
            if(board2[i][col]==0): #선택한 칸이 빈칸이라면 -> 고려하지 않음
                continue
            row=i
            while 1:
                if(row==0 or row==n): #이미 도착지점인 경우 // 모두 탐색한 경우 탈출
                    break
                if(board2[row-1][col]==0): #바로 위 칸이 빈칸이라면 -> 갈 수 있음
                    board2[row-1][col]=board2[row][col] #현재 숫자를 한 칸 위 칸으로
                    board2[row][col]=0 #원래 칸은 빈 칸이됨
                elif(board2[row-1][col]==board2[row][col] and board2[row-1][col]>0): #만약 위쪽 칸이 빈칸이 아니고(by elif) 자신과 같으며 이전에 더해지지 않았다면(board2[-1][]>0)
                    board2[row-1][col]+=board2[row][col] #두 수를 더하고
                    board2[row][col]=0 #원래 칸은 빈칸이 되고
                    board2[row-1][col]*=(-1) #더해진 칸은 (-)로 표현해 이미 더해졌음을 표시, 한 줄 이동이 끝나면 (+)로 바꿔야함
                
                row-=1 #왜 +가 아니라 -임? 이해를 못하겠네?
        
        for row in range(n):
            if(board2[row][col]>0):
                continue
            board2[row][col]*=(-1)

def move_down(): #d==1일 때
    for col in range(n):
        for i in range(n-1,-1,-1):
            if(board2[i][col]==0):
                continue
            row=i
            while 1:
                if(row==n-1):
                    break
                if(board2[row+1][col]==0):
                    board2[row+1][col]=board2[row][col]
                    board2[row][col]=0
                elif(board2[row+1][col]==board2[row][col] and board2[row+1][col]>0):
                    board2[row+1][col]+=board2[row][col]
                    board2[row][col]=0
                    board2[row+1][col]*=(-1)
                row+=1 
                if(row<=0): #이 부분 수정 필요
                    break

        for row in range(n):
            if(board2[row][col]>0):
                continue
            board2[row][col]*=(-1)

                      
def get_board_max():
    board_max=0
    for line in board2:
        board_max=max(board_max,max(line))
    return board_max

                      
init_board2()
maxi=0
for case in range(4**5):
    brute=case
    init_board2()
    for i in range(5):
        #여기서 board2 초기화
        d=brute%4 #0 ~ 3 
        brute=brute//4
        if(d==0):
            move_up()
        elif(d==1):
            move_down()
        elif(d==2):
            move_left()
        else: #d==3
            move_right()

        # 00000 ~ 33333[4]
    
    maxi=max(maxi,get_board_max())

print(maxi)


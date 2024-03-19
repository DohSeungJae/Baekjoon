
class SudokuSolver:
    def solve(self,b:list)->None:
        self.__board=b

        next_row,next_col=self.__find_next_empty()
        if(next_row==9 and next_col==9):
            return 
        
        for i in range(1,9+1):
            self.__bt(next_row,next_col,i)

    def __check_row(self,row:int,num:int)->bool:
        for x in range(9):
            if(self.__board[row][x]==num):
                return False
        return True
        
    def __check_col(self,col:int,num:int)->bool:
        for y in range(9):
            if(self.__board[y][col]==num): #!!!!
                return False
        return True
        
    def __check_33(self,row:int,col:int,num:int)->bool:
        box_x=int(col/3)*3
        box_y=int(row/3)*3
        for y in range(box_y,box_y+3):
            for x in range(box_x,box_x+3):
                if(self.__board[y][x]==num):
                    return False
        return True
    
    def __find_next_empty(self):
        for y in range(0,9):
            for x in range(0,9):
                if(self.__board[y][x]==0):
                    return [y,x]
        return [9,9]
        
    def __bt(self,row:int,col:int,num:int)->bool:
        if(not self.__check_row(row,num)):
            return False
        elif(not self.__check_col(col,num)):
            return False
        elif(not self.__check_33(row,col,num)):
            return False

        self.__board[row][col]=num
        next_row,next_col=self.__find_next_empty()

        if(next_row==9 and next_col==9):
            return True
            
        for next_num in range(1,10):
            if(self.__bt(next_row,next_col,next_num)):
                return True
            
        self.__board[row][col]=0
        return False
        
board=[]
solver=SudokuSolver()

for y in range(9):
    line=input().strip()
    temp=[int(i) for i in line]
    for x in range(len(temp)):
        integer=temp[x]
    
    board.append(temp)

solver.solve(board)
for row in board:
    for x in row:
        print(x,end="")
    print()

#참조 : https://colab.research.google.com/github/NoCodeProgram/CodingTest/blob/main/backTracking/solveSudoku.ipynb#scrollTo=Iq2FVfvsPj2R
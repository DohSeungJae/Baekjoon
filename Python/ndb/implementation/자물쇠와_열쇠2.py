def rotate_right(key):
    m=len(key)
    res=[[0]*m for _ in range(m)]
    
    for y in range(m):
        for x in range(m):
            res[y][x]=key[m-1-x][y]
    
    return res

def is_possible(new_lock):
    n=len(new_lock)//3
    for y in range(n,2*n):
        for x in range(n,2*n):
            if(new_lock[y][x]!=1):
                return False
    return True

    
    
def solution(key, lock):
    n=len(lock)
    new_lock=[[0]*(3*n) for _ in range(3*n)]
    
    for y in range(n):
        for x in range(n):
            new_lock[y+n][x+n]=lock[y][x]

            
    for _ in range(4):
        key=rotate_right(key)
        for y in range(2*n):
            for x in range(2*n): #범위 설정
                m=len(key)
                for i in range(m):
                    for j in range(m): #홈 추가
                        new_lock[y+i][x+j]+=key[i][j]
                
                if(is_possible(new_lock)):
                    return True
                  
                for i in range(m):
                    for j in range(m): #계산값 되돌림
                        new_lock[y+i][x+j]-=key[i][j]
    
    #맞는 경우가 하나도 없다면 불가능함              
    return False

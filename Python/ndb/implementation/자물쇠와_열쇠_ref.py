def turn_right(key):
    m=len(key)
    turned=[[0]*m for _ in range(m)]
    for y in range(m):
        for x in range(m):
            turned[y][x]=key[(m-1)-x][y]
            
    return turned

def check(new_lock):
    lock_len=len(new_lock)//3
    for y in range(lock_len, lock_len*2):
        for x in range(lock_len, lock_len*2):
            if(not new_lock[y][x]==1):
                return False
            
    return True

def solution(key, lock):
    n=len(lock)
    m=len(key)
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    for y in range(n,2*n):
        for x in range(n,2*n):
            new_lock[y][x]=lock[y-n][x-n]
    
    for rotate in range(4):
        key=turn_right(key)

        for y in range(2*n):
            for x in range(2*n):
                for i in range(m):
                    for j in range(m):
                        new_lock[y+i][x+j]+=key[i][j]
                        
                if(check(new_lock)==True):
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[y+i][x+j]-=key[i][j]
            
    return False
    
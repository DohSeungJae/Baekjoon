import sys
input=sys.stdin.readline

N,B=map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))

def matrixMultiple(a:list,b:list)->list:
    res=[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j]+=a[i][k]*b[k][j]
    
    return res

def matrixPower(a:list,b:int)->list:
    if(b==1):
        return [[x%1000 for x in row] for row in a]
    elif(b%2==0):
        temp=matrixPower(a,b//2)
        return [[x%1000 for x in row] for row in matrixMultiple(temp,temp)]
    else:
        temp=matrixPower(a,b//2)
        return [[x%1000 for x in row] \
                for row in matrixMultiple(a,matrixMultiple(temp,temp))]
    

matrix=(matrixPower(A,B))
for row in matrix:
    print(' '.join(map(str,row)))

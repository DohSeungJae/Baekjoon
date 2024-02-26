import sys
input=sys.stdin.readline
MOD=10**9
LEN=2
F=[[1,1],[1,0]]

def matrixMultiple(a:list,b:list)->list:
    res=[[0 for _ in range(LEN)] for _ in range(LEN)]

    for i in range(LEN):
        for j in range(LEN):
            for k in range(LEN):
                res[i][j]+=a[i][k]*b[k][j]
    return res

def fiboMatrix(a:list,b:int)->list:
    if(b==1):
        return [[x%MOD for x in row] for row in a]
    elif(b%2==0):
        temp=fiboMatrix(a,b//2)
        return [[x%MOD for x in row] for row in matrixMultiple(temp,temp)]
    else:
        temp=fiboMatrix(a,b//2)
        return [[x%MOD for x in row] \
                for row in matrixMultiple(a,matrixMultiple(temp,temp))]

t=int(input())
for _ in range(t):
    n=int(input())
    print(fiboMatrix(F,n)[0][1])
    
import sys
input=sys.stdin.readline
LEN=2
MOD=1000000000
F=[[1,1],[1,0]]

def matrixMultiple(a:list,b:list)->list:
    res=[[0 for _ in range(LEN)] for _ in range(LEN)]

    for i in range(LEN):
        for j in range(LEN):
            for k in range(LEN):
                res[i][j]+=a[i][k]*b[k][j]
    return res

def matrixPower(a:list,b:int)->list:
    if(b==1):
        return [[x%MOD for x in row] for row in a]
    elif(b%2==0):
        temp=matrixPower(a,b//2)
        return [[x%MOD for x in row] for row in matrixMultiple(temp,temp)]
    else:
        temp=matrixPower(a,b//2)
        return [[x%MOD for x in row] \
                for row in matrixMultiple(a,matrixMultiple(temp,temp))]


a,b=map(int,input().split())
print((matrixPower(F,b+2)[0][1]-matrixPower(F,a+1)[0][1])%MOD)


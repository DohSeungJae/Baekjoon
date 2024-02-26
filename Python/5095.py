import sys
input=sys.stdin.readline

def matrixMultiple(a:list,b:list)->list:
    res=[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j]+=a[i][k]*b[k][j]
    return res

def matrixPower(a:list,b:int)->list:
    if(b==1):
        return [[x%M for x in row] for row in a]
    elif(b%2==0):
        temp=matrixPower(a,b//2)
        return [[x%M for x in row] for row in matrixMultiple(temp,temp)]
    else:
        temp=matrixPower(a,b//2)
        return [[x%M for x in row] \
                for row in matrixMultiple(a,matrixMultiple(temp,temp))]
    
while 1:
    N,M,P=map(int,input().split())
    if(N==0 and M==0 and P==0):
        break
    mat=[]
    for _ in range(N):
        mat.append(list(map(int,input().split())))    

    for row in matrixPower(mat,P):
        print(*row)
    print()
    
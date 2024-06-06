import sys
input=sys.stdin.readline

a,r,n,mod=map(int,input().split())
mat=[[r,0],[a,1]]
LEN=2
def matrixMultiple(a:list,b:list)->list:
    res=[[0 for _ in range(LEN)] for _ in range(LEN)]

    for i in range(LEN):
        for j in range(LEN):
            for k in range(LEN):
                res[i][j]+=a[i][k]*b[k][j]
    return res

def matrixPower(a:list,b:int)->list:
    if(b==1):
        return [[x%mod for x in row] for row in a]
    elif(b%2==0):
        temp=matrixPower(a,b//2)
        return [[x%mod for x in row] for row in matrixMultiple(temp,temp)]
    else:
        temp=matrixPower(a,b//2)
        return [[x%mod for x in row]\
                for row in matrixMultiple(a,matrixMultiple(temp,temp))]
    

    
sn=matrixPower(mat,n)
print(sn[1][0])

    

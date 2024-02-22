import sys
input=sys.stdin.readline
LEN=2
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
        return [[x%10000 for x in row] for row in a]
    elif(b%2==0):
        temp=matrixPower(a,b//2)
        return [[x%10000 for x in row] for row in matrixMultiple(temp,temp)]
    else:
        temp=matrixPower(a,b//2)
        return [[x%10000 for x in row] \
                for row in matrixMultiple(a,matrixMultiple(temp,temp))]

n=0
while n!=-1:
    n=int(input())
    if(n==-1):
        break
    elif(n==0):
        print(0)
    elif(n==1 or n==2):
        print(1)    
    elif(n>=3):
        print(matrixPower(F,n-1)[0][0])
    


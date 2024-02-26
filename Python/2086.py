import sys
input=sys.stdin.readline
LEN=2
MOD=1000000000
F=[[1,1],[1,0]]
table={}

def matrixMultiple(a:list,b:list)->list:
    res=[[0 for _ in range(LEN)] for _ in range(LEN)]

    for i in range(LEN):
        for j in range(LEN):
            for k in range(LEN):
                res[i][j]+=a[i][k]*b[k][j]
    return res

def matrixPower(a:list,b:int)->list:
    if(b==1):
        returnValue=[[x%MOD for x in row] for row in a]
    elif(b%2==0):
        temp=matrixPower(a,b//2)
        returnValue= [[x%MOD for x in row] for row in matrixMultiple(temp,temp)]
    else:
        temp=matrixPower(a,b//2)
        returnValue= [[x%MOD for x in row] \
                for row in matrixMultiple(a,matrixMultiple(temp,temp))]
        
    if((b) not in table.keys()):
        table[b]=returnValue[0][1]
    return returnValue


start,end=map(int,input().split())
res=0

for n in range(end,start-1,-1):
    if(n==0):
        continue 
    elif(n==1 or n==2):
        res+=1
    else:
        if(n in table.keys()):
            res+=table[n]
        else:
            res+=matrixPower(F,n-1)[0][0]

print(res)
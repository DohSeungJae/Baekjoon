import sys
input=sys.stdin.readline

N=int(input())
matrixes=[]
for _ in range(N):
    matrixes.append(list(map(int,input().split())))
    
def multiply(y:int,x:int)->list[int,int]:
    if(x==1):
        return 0,matrixes[y-1]
    elif(multiplied[y][x]==[-1,-1]):
        return -1,[-1,-1]
    a=multiplied[y][x-1][:]
    b=matrixes[(x+y-2)%N][:]

    eq=0
    for i in range(2):
        for j in range(2):
            if(a[i]==b[j]):
                eq=a[i]
                break
    if(eq==0):
        return -1,[-1,-1]
    
    a.remove(eq)
    b.remove(eq)
    return a[0]*b[0]*eq,[a[0],b[0]]
    
dp=[[0 for _ in range(N+1)] for _ in range(N+1)]
dp[0][N]=sys.maxsize    
multiplied=[[[0,0] for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    multiplied[i][1]=matrixes[i-1]

for y in range(1,N+1):
    for x in range(1,N+1):
        operations,multiplied[y][x]=multiply(y,x)
        if(operations==-1):
            dp[y][x]=sys.maxsize
        else:
            dp[y][x]=dp[y][x-1]+operations
    dp[y][-1]=min(dp[y][-1],dp[y-1][-1])


print(dp)

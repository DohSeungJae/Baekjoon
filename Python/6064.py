import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    m,n,x,y=map(int,input().split())

    b=0
    while (x<=m*n):
        if(x%n==y%n):
            b=x
            break
        else:
            x+=m

    if(b==0):
        print(-1)
    else:
        print(b)
        

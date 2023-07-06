import sys
input=sys.stdin.readline
a=[]
b=[]
c=[]

n,m=map(int,input().split())
for _ in range(n):
    a.append(list(map(int,input().split())))

m,k=map(int,input().split())
for _ in range(m):
    b.append(list(map(int,input().split())))


for i in range(n):
    for j in range(k):
        c=0
        for h in range(m):
            c+=a[i][h]*b[h][j]
        print(c,end=" ")
        
    print()






    

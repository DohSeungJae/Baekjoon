import sys
input=sys.stdin.readline

mat1=[]
mat2=[]

n,m=map(int,input().split())

for _ in range(n):
    mat1.append(list(map(int,input().split())))

for _ in range(n):
    mat2.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        mat1[i][j]=mat1[i][j]+mat2[i][j]
        print(mat1[i][j],end=" ")
    
    print()
    

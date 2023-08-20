import sys
input=sys.stdin.readline

n=int(input())
mat1=[list(map(int,input().split())) for _ in range(n)]
mat2=[list(map(int,input().split())) for _ in range(n)]

cnt=0
for i in range(n):
    for j in range(n):
        c=0
        for h in range(n):
            c+=mat1[i][h]*mat2[h][j]
        if(c):
            cnt+=1

print(cnt)

#부울행렬의 부울곱

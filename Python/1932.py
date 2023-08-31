import sys
input=sys.stdin.readline

tri=[]
n=int(input())
for _ in range(n):
    tri.append(list(map(int,input().split())))

tri.append([0 for _ in range(n+1)])

for i in range(n-1,-1,-1):
    for j in range(i+1):
        tri[i][j]+=max(tri[i+1][j],tri[i+1][j+1])

print(tri[0][0])




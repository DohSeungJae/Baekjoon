import sys
input=sys.stdin.readline

n,m=map(int,input().split())
table=[]
table_sum=[[0]*(n+1) for _ in range(n+1)]

for _ in range(n):
    table.append(list(map(int,input().split())))

table_sum[1][1]=table[0][0]


for y in range(1,n+1):
    for x in range(1,n+1):
        table_sum[y][x]=table[y-1][x-1]+table_sum[y-1][x]+table_sum[y][x-1]-table_sum[y-1][x-1]

for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(table_sum[x2][y2]-table_sum[x2][y1-1]-table_sum[x1-1][y2]+table_sum[x1-1][y1-1])
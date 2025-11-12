from itertools import combinations
import sys

def get_dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

n,m=map(int,input().split())
board=[]
chick=[]
home=[]

for y in range(n):
    line=list(map(int,input().split()))
    board.append(line)
    for x in range(n):
        if(line[x]==1):
            home.append([y,x])
        elif(line[x]==2):
            chick.append([y,x])

result=sys.maxsize
for chic in combinations(chick,m):
    sum_chick=0
    for h in home:
        min_chick=sys.maxsize
        for c in chic:
            chick_dist=get_dist(h,c)
            min_chick=min(min_chick,chick_dist)
        sum_chick+=min_chick
    
    result=min(result,sum_chick)

print(result)
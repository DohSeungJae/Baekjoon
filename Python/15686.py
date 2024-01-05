import sys
from itertools import combinations
input=sys.stdin.readline

n,m=map(int,input().split())
board=[]
cnt2=0
cords2=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    if 2 in temp:
        for i in range(n):

elements = [i for i in range(1, m+1)]  # 예: [1,2,3,4,5]
  
for combo in combinations(elements, n):
    print(combo)

        
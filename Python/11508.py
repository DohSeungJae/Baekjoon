import sys
input=sys.stdin.readline

N=int(input())
budget=[]
for _ in range(N):
    budget.append(int(input()))
budget.sort(reverse=True)
totalCost=0

for i in range(N):
    if(i%3==2):
        continue
    totalCost+=budget[i]
    
print(totalCost)
import sys
input=sys.stdin.readline

n=int(input())
budgets=list(map(int,input().split(" ")))
m=int(input())
start=0
end=max(budgets)
mid=0

if(sum(budgets)<=m):
    print(max(budgets))
    exit(0)

while start<=end:
    mid=(start+end)//2
    budget=0
    for i in budgets:
        if i>mid: #예산이 상한값 초과
            budget+=mid #상한값만 더함
        else:
            budget+=i 
    
    if budget > m : #합계가 총 예산 초과
        end=mid-1
    else: #합계가 총 예산 미만
        start=mid+1


print(end)



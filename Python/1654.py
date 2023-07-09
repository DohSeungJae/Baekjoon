import sys
input=sys.stdin.readline

n,k=map(int,input().split())

l_list=[]
for _ in range(n):
    l_list.append(int(input()))

start=1
end=max(l_list)
mid=0

while start<=end:
    mid=int((start+end)/2)
    num=0
    for i in l_list:
        num+=i//mid
    
    if num>=k: #조건 만족,  최댓값 탐색이므로 더 큰 값(오른쪽) 탐색,
        start=mid+1
    
    else: #num<k 조건 만족 x
        end=mid-1


print(end)

#랜선 자르기


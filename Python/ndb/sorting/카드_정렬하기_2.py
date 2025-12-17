import heapq

n=int(input())
hq=[]

for _ in range(n):
    heapq.heappush(hq,int(input()))

ans=0
while len(hq)>1:
    tmp=heapq.heappop(hq)+heapq.heappop(hq)
    heapq.heappush(hq,tmp)
    ans+=tmp

print(ans)

#반복적으로 최소값을 빠르게 찾아야 하는 경우 
#우선순위 큐가 효율적임 


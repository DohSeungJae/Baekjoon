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
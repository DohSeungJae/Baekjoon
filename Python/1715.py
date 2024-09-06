import sys
import heapq
input=sys.stdin.readline

N=int(input())
hq=[]
totalCal=0
for _ in range(N):
    heapq.heappush(hq,int(input()))

while len(hq)>1:
    a=heapq.heappop(hq)
    b=heapq.heappop(hq)
    totalCal+=(a+b)
    heapq.heappush(hq,(a+b))

print(totalCal)
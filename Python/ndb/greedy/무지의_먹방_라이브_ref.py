import heapq

def solution(food_times, k):
    if(sum(food_times)<=k):
        return -1
    
    hq=[]
    for i in range(len(food_times)):
        heapq.heappush(hq,(food_times[i],i+1))
    
    length=len(food_times)
    prev=0
    time_spent=0
    while(time_spent+(hq[0][0]-prev)*length<=k):
        now=heapq.heappop(hq)[0]
        time_spent+=(now-prev)*length
        length-=1
        prev=now

    result=sorted(hq,key=lambda x:x[1])
    return result[(k-time_spent)%length][1]
import heapq

def solution(food_times, k):
    if(sum(food_times)<=k):
        #시간이 sum(food_times) 만큼 지나면 이제 남은 음식이 없음
        #다음 먹을 음식을 이제 지정할 수가 없다는 의미 -> 더 섭취해야할 음식이 없음 -> return -1
        return -1
    
    hq=[]
    length=len(food_times)
    for i in range(length):
        heapq.heappush(hq,(food_times[i],i+1))
    
    time_spent=0
    prev=0
    while(time_spent+((hq[0][0]-prev)*length)<=k): #어떤 음식을 다 먹을 수 있다면 아래 실행
        #시간이 적게 걸리는 음식부터 위 조건을 확인하기 위해 힙큐 사용 
        now=heapq.heappop(hq)[0] #현재 음식을 먹는데 걸리는 시간
        time_spent+=(now-prev)*length #length를 곱하는 이유는 하나의 음식만 먹는게 아니라
        #돌아가면서 다른 음식도 먹기 때문
        #now-prev인 이유는 이전에 어떤 음식을 다 먹었다면, 그 과정에서 현재 먹는 음식도
        #prev만큼 먹었을 것이기 때문.
        
        #여기서 now-prev가 음수가 아님을 보장할 수 있음.
        #now는 hq(Python에서는 기본적으로 최소힙이기 때문에)를 사용해 
        #항상 작은 순서대로 데이터를 가져오는데
        #이전에 뽑은 것 보다(prev) 지금 뽑은 것(now)이 항상 큼
        #따라서 now-prev는 음수가 될 수 없음
        
        
        length-=1
        #현재 음식을 다 먹었기 때문에 길이 1 감소
        prev=now
        #현재 음식을 먹는데 걸리는 시간은 다음 과정에서 prev로 사용됨

    #while 문에서 나왔다는 것은 더이상 "다" 먹을 수 있는 음식이 없다는 의미
    #하지만 네트워크가 끊기기 전에 음식을 더 먹을 수는 있음(?).
    
    #그런데 while문을 탈출했을 때
    #아직 네트워크가 끊기기 전이라는 것을 어떻게 보장할 수 있나?
    # -> 맨 처음 if문에서는
    #네트워크가 끊기기 전에 다 먹을 수 있는 경우를 미리 배제했음
    #그럼 위 if문에서 걸러지지 않았다는 것은
    #네트워크가 끊기기 전에 음식을 다 먹을 수 없다는 의미
    #따라서 while문을 나와도 더 먹을 음식이 "무조건"남아 있음
    
    #전술했듯이 while문을 "다" 먹을 수 있는 음식은 이제 없음
    #이제 다음 먹을 음식을 지정해야하는데, 음식은 원래 순서대로 먹기 때문에
    #음식 순서를 기준으로 정렬
    result=sorted(hq ,key=lambda x:x[1])
    
    #(k-time_spent) 앞으로 몇 번 더 먹을 수 있냐를 의미
    #%length 연산을 통해 (k-time_spent)번 만큼 앞으로 갔을 때 어느 위치인지 계산
    #그 값을 반환
    return result[(k-time_spent)%length][1]
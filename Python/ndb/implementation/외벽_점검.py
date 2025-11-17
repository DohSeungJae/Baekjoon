from itertools import permutations

def solution(n, weak, dist):
    answer=len(dist)+1
    length=len(weak)
    
    for i in range(length):
        weak.append(weak[i]+n)
    
    for friends in permutations(dist,len(dist)):
        for start in range(length):
            cnt=1
            position=weak[start]+friends[cnt-1]
            for idx in range(start,start+length):
                if(position<weak[idx]):
                    cnt+=1
                    if(cnt>len(dist)):
                        break
                    position=weak[idx]+friends[cnt-1]
        
            answer=min(answer,cnt)
            
    if(answer>len(dist)):
        answer= -1
        
    return answer
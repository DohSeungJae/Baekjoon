def solution(N, stages):
    answer = []
    cnt=[0]*(N+2)
    for i in stages:
        cnt[i]+=1
        
    tmp=[]
    rest=len(stages)
    for i in range(1,N+1):
        if(rest==0):
            tmp.append((0,i))
            continue
        tmp.append((cnt[i]/rest,i))
        rest-=cnt[i]
          
    tmp.sort(key=lambda x:-x[0])
    for i in tmp:
        answer.append(i[1])

    return answer
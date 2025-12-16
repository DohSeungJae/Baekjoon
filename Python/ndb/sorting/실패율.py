def solution(N, stages):
    answer = []
    tmp=[]
    rest=len(stages)
    cnt=[0]*(N+2)
    for stage in stages:
        cnt[stage]+=1
    for i in range(1,N+1):
        '''
        percent=cnt[i]/rest
        오답 코드 -> 0으로 나누는 경우를 고려하지 않음 
        ''' 

        ### 정답 코드 
        if(rest==0): #!!!

            percent=0
        else:
            percent=cnt[i]/rest
            #나눗셈 연산이 있을 때
            #0으로 나누는 경우를 반드시 고려해야함
        ###
        tmp.append((percent,i))
        rest-=cnt[i]
        
    tmp.sort(key=lambda x:-x[0])
    for i in tmp:
        answer.append(i[1])
    
    return answer
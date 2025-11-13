def is_possible(answer):
    for frame in answer: 
        #모든 구조물을 탐색하면서 조건에 맞는지 확인
        #이미 구조물을 추가/삭제한 상태에서 실행됨
    
        x,y,a=frame
        if(a==0): #기둥
            if(y==0 or [x,y,1] in answer or [x-1,y,1] in answer or [x,y-1,0] in answer):
                continue
            return False
        else: #a==1 보
            if([x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer)):
                continue
            return False
    
    return True

def solution(n, build_frame):
    answer=[] #현재 구조물을 저장한 배열 
    for build in build_frame:
        x,y,a,b=build
        if(b==0): #삭제
            answer.remove([x,y,a]) 
            #미리 삭제하고 가능 여부는 그 이후에 판단
            possible=is_possible(answer)
            if(not possible): #삭제했을 때 조건이 맞지 않다면 다시 되돌림 -> 추가
                answer.append([x,y,a])
            
        else: #b==1 #설치
            answer.append([x,y,a]) 
            #먼저 설치하고 가능 여부는 그 이후에 판단
            possible=is_possible(answer)
            if(not possible): #추가했을 때 조건이 맞지 않다면 다시 되돌림 -> 삭제 
                answer.remove([x,y,a])
            
    return sorted(answer)
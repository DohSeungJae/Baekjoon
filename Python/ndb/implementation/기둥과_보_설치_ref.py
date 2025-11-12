def is_possible(answer):
    for x,y,a in answer:
        if(a==0):
            if(y==0 or [x,y,1] in answer or [x-1,y,1] in answer or [x,y-1,0] in answer):
                continue
            return False
        else:
            if([x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer)):
                continue
            return False
        
    return True

def solution(n, build_frame):
    answer=[]
    for build in build_frame:
        x,y,a,b=build
        if(b==0): #삭제
            answer.remove([x,y,a])
            possible=is_possible(answer)
            if(not possible): answer.append([x,y,a])
        else: #b==1 # 추가 
            answer.append([x,y,a])
            possible=is_possible(answer)
            if(not possible): answer.remove([x,y,a])

    return sorted(answer)
def get_balanced(p):
    cnt=0
    for i in range(len(p)):
        if(p[i]=='('):
            cnt+=1
        else:
            cnt-=1
        if(cnt==0):
            return i

def check_right(p):
    cnt=0
    for i in range(len(p)):
        if(p[i]=='('):
            cnt+=1
        else:
            cnt-=1
            if(cnt==0):
                return True
    return False


def solution(p):
    answer = ''
    if(p==''):
        return p
    idx=get_balanced(p)
    u=p[:idx+1]
    v=p[idx+1:]
    if(check_right(u)):
        answer=u+solution(v)
        return answer
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        u=u[1:-1]
        for i in range(len(u)):
            if(u[i]=='('):
                answer+=')'
            else:
                answer+='('
        
        return answer
    

stk=[]
def bt(mx):
    if(len(stk)==m):
        print(*stk)
        return 
    for i in range(1,n+1):
        if((i not in stk) and i>mx):
            stk.append(i)
            bt(i)
            stk.pop()
                 
n,m=map(int,input().split())
bt(0)


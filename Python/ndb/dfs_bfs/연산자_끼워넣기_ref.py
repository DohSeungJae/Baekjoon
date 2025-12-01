n=int(input())
nums=list(map(int,input().split()))
op=list(map(int,input().split())) #덧셈, 뺄셈, 곱셈, 나눗셈

mini=1000000000
maxi=-(1000000000)
#idx 초기값 0, tmp 초기값 nums[0]
def dfs(idx,tmp):
    global mini, maxi
    if(idx==(n-1)): #연산을 n-1번 하면 끝남
        maxi=max(maxi,tmp)
        mini=min(mini,tmp)
        return
    
    nxt=nums[idx+1]
    for oper in range(4):
        if(oper==0 and op[oper]>0): #덧
            op[oper]-=1
            dfs(idx+1,tmp+nxt)
            op[oper]+=1
        if(oper==1 and op[oper]>0): #뺄
            op[oper]-=1
            dfs(idx+1,tmp-nxt)
            op[oper]+=1
        if(oper==2 and op[oper]>0): #곱
            op[oper]-=1
            dfs(idx+1,tmp*nxt)
            op[oper]+=1
        if(oper==3 and op[oper]>0): #나
            op[oper]-=1
            if(tmp>0):
                dfs(idx+1,tmp//nxt)
                op[oper]+=1
            else:
                dfs(idx+1, -((-tmp)//nxt))
                op[oper]+=1


dfs(0,nums[0])
print(maxi)
print(mini)




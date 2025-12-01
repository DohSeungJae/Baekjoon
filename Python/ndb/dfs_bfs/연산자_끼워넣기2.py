MAX=-1000000000
MIN=1000000000

def dfs(idx,tmp):
    global MIN,MAX
    if(idx==(n-1)):
        MIN=min(MIN,tmp)
        MAX=max(MAX,tmp)
        return 
    for i in range(4):
        if(i==0 and op[i]>0):
            op[i]-=1
            dfs(idx+1,tmp+lst[idx+1])
            op[i]+=1
        elif(i==1 and op[i]>0):
            op[i]-=1
            dfs(idx+1,tmp-lst[idx+1])
            op[i]+=1
        elif(i==2 and op[i]>0):
            op[i]-=1
            dfs(idx+1,tmp*lst[idx+1])
            op[i]+=1
        elif(i==3 and op[i]>0):
            op[i]-=1
            if(tmp<0):
                dfs(idx+1,-((-tmp)//lst[idx+1]))
            else:
                dfs(idx+1, tmp//lst[idx+1])
            op[i]+=1

n=int(input())
lst=list(map(int,input().split()))
op=list(map(int,input().split())) #[덧셈, 뺄셈, 곱셈, 나눗셈]

dfs(0,lst[0])
print(MAX)
print(MIN)
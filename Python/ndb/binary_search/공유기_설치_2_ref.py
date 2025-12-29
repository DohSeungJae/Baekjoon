n,c=map(int,input().split())
lst=sorted([int(input()) for _ in range(n)])

res=0
start=1 #min gap
end=lst[-1]-lst[0] #max gap
while not(start>end):
    mid=(start+end)//2
    value=lst[0]
    cnt=1

    for i in range(1,n):
        if(lst[i]-value>=mid):
            value=lst[i]
            cnt+=1
    
    if(cnt>=c):
        res=mid
        start=mid+1
    else:
        end=mid-1

print(res)


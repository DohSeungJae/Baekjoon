n,m=map(int,input().split())
lst=sorted(list(map(int,input().split())))

res=0
start=lst[0]
end=lst[-1]
while not(start>end):
    mid=(start+end)//2

    rest=0
    for i in range(n):
        if(lst[i]-mid>0):
            rest+=(lst[i]-mid)

    if(rest>=m):
        res=mid
        start=mid+1
    else:
        end=mid-1

print(res)

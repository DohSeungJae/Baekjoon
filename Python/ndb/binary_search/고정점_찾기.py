def bs(start,end,lst):
    if(start>end):
        return None
    mid=(start+end)//2
    value=lst[mid]
    #인덱스(mid)>value인 경우 오른쪽으로
    #인덱스(mid)<value인 경우 왼쪽으로
    if(mid==value):
        return mid
    elif(mid>value):
        return bs(mid+1,end,lst)
    else:
        return bs(start,mid-1,lst)
    

n=int(input())
lst=list(map(int,input().split()))
idx=bs(0,n-1,lst)
if(idx==None):
    print(-1)
    exit(0)
print(idx)
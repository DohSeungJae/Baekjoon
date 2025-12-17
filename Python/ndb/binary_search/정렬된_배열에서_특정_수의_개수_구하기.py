def bs_left(start,end,target,lst):
    global idx_left
    if(start>end):
        return None
    m=(start+end)//2
    if(lst[m]==target):
        idx_left=m
        return bs_left(start,m-1,target,lst)
    elif(lst[m]>target):
        return bs_left(start,m-1,target,lst)
    else: #lst[m]<target
        return bs_left(m+1,end,target,lst)

def bs_right(start,end,target,lst):
    global idx_right
    if(start>end):
        return None
    m=(start+end)//2
    if(lst[m]==target):
        idx_right=m
        return bs_right(m+1,end,target,lst)
    elif(lst[m]>target):
        return bs_right(start,m-1,target,lst)
    else: #lst[m]<target
        return bs_right(m+1,end,target,lst)

n,target=map(int,input().split())
lst=list(map(int,input().split()))

idx_left=-1
idx_right=-1
bs_left(0,n-1,target,lst)
bs_right(0,n-1,target,lst)

if(idx_left==-1 and idx_right==-1):
    print(-1)
    exit(0)

print(idx_right-idx_left+1)

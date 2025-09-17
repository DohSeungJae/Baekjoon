import sys
input=sys.stdin.readline

def get_rest(array,H):
    rest=0
    for i in range(N):
        if(array[i]>H):
            rest+=(array[i]-H)
    return rest

def binary_search(array,start,end):
    if(start>end):
        return 
    
    mid=(start+end)//2
    
    m=get_rest(array,mid)
    if(m>=M):
        global res
        res=max(res,mid)
        return binary_search(array,mid+1,end)
    else:
        return binary_search(array,start,mid-1)
    
N,M=map(int,input().split())
array=list(map(int,input().split()))

res=0
binary_search(array,0,max(array))
print(res)


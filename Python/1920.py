#1920
import sys
input=sys.stdin.readline

n=int(input())
n_list=list(map(int,input().split(" ")))
n_list.sort()


def bs(start,mid,end,target):
    if start>end:
        return None
    
    mid=(start+end)//2
    
    if n_list[mid]==target:
        return mid
    elif target<n_list[mid]:
        end=mid-1
        return bs(start,mid,mid-1,target)
    elif target>n_list[mid]:
        start=mid+1
        return bs(mid+1,mid,end,target)


m=int(input())
targets=list(map(int,input().split()))

for i in range(m):
    target=targets[i]
    mid=int(n-1*0.5)
    idx=bs(0,mid,n-1,target)

    if(idx!=None):
        print(1)
    else:
        print(0)
    



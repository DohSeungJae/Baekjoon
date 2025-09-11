import sys
input=sys.stdin.readline


def binary_search(array,target,start,end):
    if(start>end):
        return None
    mid=(start+end)//2
    if(array[mid]==target):
        return target
    elif(array[mid]>target):
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
    

N=int(input())
array=list(map(int,input().split()))
M=int(input())
requires=list(map(int,input().split()))

for require in requires:
    idx=binary_search(array,require,0,N-1)
    if(idx==None):
        print("no")
    else:
        print("yes")



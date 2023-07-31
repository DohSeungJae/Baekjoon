import sys
input=sys.stdin.readline

n,m=map(int,input().split())

w_list=list(map(int,input().split()))

start=1
end=max(w_list)

while start<=end:
    mid=(start+end)//2
    rest=0
    for w in w_list:
        if(w>=mid): rest+=w-mid

    if rest>=m:
        start=mid+1
    else:
        end=mid-1


print(end)

#나무 자르기

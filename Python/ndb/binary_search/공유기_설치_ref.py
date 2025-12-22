def solution():
    n,c=map(int,input().split())
    lst=sorted([int(input()) for _ in range(n)])

    result=0
    start=1 #가능한 최소 거리 
    end=lst[-1]-lst[0] #가능한 최대 거리
    while not(start>end):
        mid=(start+end)//2
        cnt=1
        value=lst[0]

        for i in range(1,n):
            if(lst[i]-value>=mid):
                value=lst[i]
                cnt+=1
        
        if(cnt>=c):
            start=mid+1
            result=mid
        else:
            end=mid-1

    print(result)

solution()

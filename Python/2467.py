import sys
input=sys.stdin.readline

n=int(input())
numList=list(map(int,input().split()))

start=0
end=n-1

absMin=sys.maxsize

while(start<end):
    sum=numList[start]+numList[end]
    absSum=abs(sum)
    if absSum<absMin:
        absMin=absSum
        ans=[numList[start],numList[end]]

    if sum<0:
        start+=1
    else:
        end-=1
        
print(*ans)


#투포인터/이분탐색 기준??

#0이면 바로 break <- 최적값이므로
#abs값이 이전 값보다 크다면 start+=1
#abs값이 이전 값보다 작으면 end+=1

#배열이 오름차순 정렬 -> start나 end 값
#어느 하나를 증가시켜도 absS값은 커짐.
#그럼 absS값이 absMin값보다 클 때는?
#start값을 맨 끝에 두고
#end값을 맨 처음에 둬서
#absS값이 absMin값보다 클 때 start-=1
#이런 방식으로 absS 값을 낮출 수 없나?
#예제를 보고 판단하자.

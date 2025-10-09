import sys
input=sys.stdin.readline

cnt=[0]*((2*1000000)+1)

n=int(input())
lst=list(map(int,input().split()))
x=int(input())
res=0

for num in lst:
    cnt[num]+=1

for num in lst:
    cnt[num]-=1
    if(x-num<=0):#이 조건문이 없어도 정답 처리는 된다..
        continue 
    if(cnt[x-num]>0):
        cnt[x-num]-=1
        res+=1

print(res)



import sys
input=sys.stdin.readline

cnt=[0]*((2*1000000)+1)

n=int(input())
lst=list(map(int,input().split()))
x=int(input())
res=0

for num in lst:
    cnt[num]=1

for num in lst:
    cnt[num]=0
    if(x-num<=0):
        continue 
    if(cnt[x-num]>0):
        cnt[x-num]=0
        res+=1

print(res)


#수정 
#수가 중복되는 경우가 없기 때문에 카운트를 계산할 필요가 없음.
#있는지 없는지만 판단하면 됨.
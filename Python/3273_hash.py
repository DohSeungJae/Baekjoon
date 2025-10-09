import sys
input=sys.stdin.readline

n=int(input())
array=list(map(int,input().split()))
x=int(input())
cnt={}
res=0

for n in array:
    if not n in cnt.keys():
        cnt[n]=1
        
for n in array:
    cnt[n]=0
    if((x-n) in cnt.keys()):
        if(cnt[x-n]==1):
            cnt[x-n]=0
            res+=1

print(res)

#수정 
#수가 중복되는 경우가 없기 때문에 카운트를 계산할 필요가 없음.
#있는지 없는지만 판단하면 됨.
            

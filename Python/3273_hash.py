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
    else:
        cnt[n]+=1

for n in array:
    cnt[n]-=1
    if((x-n) in cnt.keys()):
        if(cnt[x-n]>0):
            cnt[x-n]-=1
            res+=1

print(res)

            

n=int(input())
lst=list(map(int,input().split()))
v=int(input())

cnt=[0]*101
cnt_minus=[0]*101

for num in lst:
    if(num>=0):
        cnt[num]+=1
    else:
        num=num*(-1)
        cnt_minus[num]+=1

if(v>=0):
    print(cnt[v])
else:
    v=v*(-1)
    print(cnt_minus[v])

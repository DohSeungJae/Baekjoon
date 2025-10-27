n,m=map(int,input().split())
lst=list(map(int,input().split()))
w_cnt=[0]*(m+1)
for w in lst:
    w_cnt[w]+=1

print(w_cnt)

result=0
for i in range(1,m+1):
    n-=w_cnt[i]
    result+=(w_cnt[i]*n)

print(result)


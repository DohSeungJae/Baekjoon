n,m=map(int,input().split())
k_lst=list(map(int,input().split())) #k는 각 공의 무게
w_cnt=[0]*(m+1)

for k in k_lst:
    w_cnt[k]+=1

result=0
for w in range(1,m+1):
    n-=w_cnt[w]
    result+=(w_cnt[w]*n)

print(result)

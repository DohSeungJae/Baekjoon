n=int(input())
lst=list(map(int,input().split()))
v=int(input())
cnt=[0]*201

for num in lst:
    cnt[num+100]+=1

print(cnt[v+100])
    

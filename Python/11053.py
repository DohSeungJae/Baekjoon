import sys
input=sys.stdin.readline

n=int(input())
n_list=[0]
n_list+=list(map(int,input().split()))
dp=[0]*(n+10)

for i in range(1,n+1):
    for j in range(i):
        if(n_list[i]>n_list[j]):
            dp[i]=max(dp[i],dp[j]+1)


print(max(dp))

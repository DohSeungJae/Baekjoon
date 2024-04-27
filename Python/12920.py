import sys
input=sys.stdin.readline

N,M=map(int,input().split())
bag=[[0,0]]
for _ in range(N):
    V,C,K=map(int,input().split())
    for _ in range(K):
        bag.append([V,C])
dp=[[0]*(M+1) for _ in range(len(bag))]

for i in range(1,len(bag)):
    w=bag[i][0]
    v=bag[i][1]
    for j in range(1,M+1):
        if(j<w):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)

print(dp[-1][-1])


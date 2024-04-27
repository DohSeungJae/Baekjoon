import sys
input=sys.stdin.readline

N,M=map(int,input().split())
bag=[[0,0,0]]
maxK=0
for _ in range(N):
    V,C,K=map(int,input().split())
    maxK=max(maxK,K)
    bag.append([V,C,K])

dp=[[[0 for _ in range(maxK+1)] for _ in range(M+1)] for _ in range(N+1)]


for n in range(1,N+1):
    V=bag[n][0]
    C=bag[n][1]
    K=bag[n][2]
    for m in range(1,M+1):
        for k in range(1,maxK+1):
            km=m*k
            kc=C*k
            if(km<V):
                dp[n][m][k]=dp[n-1][m][k]
            elif(k*V>m):
                dp[n][m][k]=dp[n][m][k-1]
            else:
                dp[n][m][k]=max(dp[n-1][m][k],dp[n-1][m-k*V][k]+kc,dp[n][m][k-1])

         

print(dp[-1][-1][-1])




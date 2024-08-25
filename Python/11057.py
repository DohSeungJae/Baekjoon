import sys
input=sys.stdin.readline

dp=[0,10]
subs=[[0],[0,1,2,3,4,5,6,7,8,9]]

N=int(input())
for n in range(2,N+1):
    dp.append(10*dp[-1]-sum(subs[-1]))

    memory=[0]
    for m in range(9):
        memory.append(dp[n-1]+memory[-1]-subs[n-1][m])
    subs.append(memory)
    
print(dp[N]%10007)
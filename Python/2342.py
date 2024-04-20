import sys
input=sys.stdin.readline
INF=sys.maxsize

commands=list(map(int,input().split()))
commands.pop()
n=len(commands)
dp=[[[INF for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
dp[-1][0][0]=0

def getCost(prev:int, target:int)->int:
    if(prev==0):
        return 2
    elif(abs(target-prev)==2):
        return 4
    elif(prev==target):
        return 1
    return 3
    
for i in range(n):
    target=commands[i]
    for fixedR in range(5):
        for prevL in range(5):
            cost=getCost(prevL,target)
            dp[i][target][fixedR]=min(dp[i][target][fixedR],
                                        dp[i-1][prevL][fixedR]+cost)
    for fixedL in range(5):
        for prevR in range(5):
            cost=getCost(prevR,target)
            dp[i][fixedL][target]=min(dp[i][fixedL][target],
                                      dp[i-1][fixedL][prevR]+cost)

minCost=sys.maxsize
for l in range(5):
    for r in range(5):
        minCost=min(minCost,dp[len(commands)-1][l][r])

print(minCost)
print(dp[len(commands)-1])


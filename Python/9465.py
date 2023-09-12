import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    stk=[]
    n=int(input())
    dp=[[0 for _ in range(n)] for __ in range(2)]
    for __ in range(2):
        stk.append(list(map(int,input().split())))

    dp[0][0]=stk[0][0]
    dp[1][0]=stk[1][0]

    if(n>=2):
    
        dp[0][1]=stk[0][1]+stk[1][0]
        dp[1][1]=stk[0][0]+stk[1][1]

        for i in range(2,n):
            dp[0][i]=max(dp[1][i-2],dp[1][i-1])+stk[0][i]
            dp[1][i]=max(dp[0][i-2],dp[0][i-1])+stk[1][i]

    print(max(max(dp[0]),max(dp[1])))
    

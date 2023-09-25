import sys
input=sys.stdin.readline

strA=input().strip()
strB=input().strip()
strC=input().strip()

dp=[[[0]*(len(strA)+1) for _ in range(len(strB)+1)] for __ in range(len(strC)+1)]

for a in range(1,len(strA)+1):
    for b in range(1,len(strB)+1):
        for c in range(1,len(strC)+1):
            if(strA[a-1]==strB[b-1]==strC[c-1]):
                dp[c][b][a]=dp[c-1][b-1][a-1]+1
            else:
                dp[c][b][a]=max(dp[c][b][a-1],dp[c][b-1][a],dp[c-1][b][a])

print(dp[-1][-1][-1])
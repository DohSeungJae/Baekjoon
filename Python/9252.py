import sys
input=sys.stdin.readline

a=input().strip()
b=input().strip()

dp=[[0]*(len(a)+1) for _ in range(len(b)+1)]
isDiagonals=[[0]*(len(a)+1) for _ in range(len(b)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if(b[j-1]==a[i-1]):
            dp[j][i]=dp[j-1][i-1]+1
            isDiagonals[j][i]=1
        else:
            dp[j][i]=max(dp[j-1][i],dp[j][i-1])

unitY=len(b)
unitX=len(a)
stack=[]

while(not(unitY==0 or unitX==0)):
    if(isDiagonals[unitY][unitX]):
        stack.append(a[unitX-1])
        unitY-=1
        unitX-=1
    elif(dp[unitY-1][unitX]>=dp[unitY][unitX-1]):
        unitY-=1
    else:
        unitX-=1

print(len(stack))
print(''.join(stack[::-1]))




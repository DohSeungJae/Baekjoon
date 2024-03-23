import sys
input=sys.stdin.readline

N=int(input())
numList=list(map(int,input().split()))
M=int(input())

dp=[[1 if i==j else 0 for i in range(N)] for j in range(N)]

def processCrosses(s:int,e:int,dp:list)->None:
    while True:
        e+=1
        s-=1
        if(not(0<=e<=N-1 and 0<=s<=N-1)):
            break
        if(dp[s+1][e-1]==1 and numList[s]==numList[e]):
            dp[s][e]=1

def solution()->None:

    for i in range(N):
        if(i!=N-1 and numList[i]==numList[i+1]):
            dp[i][i+1]=1

        processCrosses(i,i,dp)
        processCrosses(i,i+1,dp)

    for _ in range(M):
        S,E=map(int,input().split())
        print(dp[S-1][E-1])

if __name__=="__main__":
    solution()


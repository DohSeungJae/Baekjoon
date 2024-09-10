import sys
input=sys.stdin.readline

N,K=map(int,input().split())
lowerLimit=(K*(K+1))//2

if(N<lowerLimit):
    print(-1)
elif((N-lowerLimit)%K)==0:
    print(K-1)
else:
    print(K)

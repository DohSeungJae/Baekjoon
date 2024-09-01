import sys
input=sys.stdin.readline

N=int(input())
cntTaller=list(map(int,input().split()))
reversedCntTaller=cntTaller[::-1]
resSeq=[]

for i in range(N):
    resSeq.insert(reversedCntTaller[i],N-i)

print(*resSeq)


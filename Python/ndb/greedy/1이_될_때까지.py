import sys
input=sys.stdin.readline

N,K=map(int,input().split())

cnt=0
while not (N==1):
    if(N<K):
        cnt+=(N-1)
        N=1
    elif(N%K!=0):
        cnt+=(N%K)
        N-=(N%K)
    else:
        N=int(N/K)
        cnt+=1

print(cnt)
#edge case missed

    
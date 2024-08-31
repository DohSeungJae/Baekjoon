import sys
input=sys.stdin.readline

N,L=map(int,input().split())
cord=list(map(int,input().split()))
cord.sort()
isTied={cord[i]:0 for i in range(N)}
cnt=0
        
for i in cord:
    if(isTied[i]==1):
        continue
    cnt+=1
    for j in cord:
        if(j-i>L-1):
            continue
        else:
            isTied[j]=1

print(cnt)
    
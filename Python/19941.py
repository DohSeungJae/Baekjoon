import sys
input=sys.stdin.readline

N,K=map(int,input().split())
table=[i for i in input().strip()]
peopleCord=[]
cnt=0

for i in range(N):
    if(table[i]=="P"):
        peopleCord.append(i)

for p in peopleCord:
    for i in range(-K,K+1):
        if(not 0<=p+i<N):
            continue
        if(table[p+i]=="H"):
            table[p+i]="X"
            cnt+=1
            break ###!!!!!!####!!!!

print(cnt)
        

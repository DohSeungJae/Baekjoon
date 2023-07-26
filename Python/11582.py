import sys
input=sys.stdin.readline

n=int(input())
c_list=list(map(int,input().split()))
k=int(input())
idx=n//k

for i in range(k):
    division=c_list[i*idx:(i+1)*idx]
    division.sort()
    for d in division:
        print(d, end=" ")
        

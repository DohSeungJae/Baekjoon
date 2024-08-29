import sys
input=sys.stdin.readline

N=int(input())
seq=list(map(int,input().split()))
gis=[0]

for i in range(N):
    if(seq[i]>gis[-1]):
        gis.append(seq[i])
    
print(len(gis)-1)
print(*gis[1:])

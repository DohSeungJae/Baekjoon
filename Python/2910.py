import sys
input=sys.stdin.readline

n,c=map(int,input().split())
d={}
l=list(map(int,input().split()))


for i in l:
    if(d.get(i)==None):
        d[i]=1
    else:
        d[i]+=1

for __ in range(len(d)):
    maxi=max(d.values())
    
    for key in d.keys():
        if(d[key]==maxi):
            for _ in range(maxi):
                print(key,end=" ")
            d[key]=-1
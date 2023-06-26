import sys
input=sys.stdin.readline

n=int(input())
l=[]
res={}

for _ in range(n):
    l.append(int(input()))
l.sort(reverse=True)

while(l):
        
    n=l.pop()
    if(res.get(n)==None):
        res[n]=1
    else:
        res[n]+=1

maxi=max(res.values())

for key in res.keys():
    if(maxi==res[key]):
        print(key)
        break






import sys
input=sys.stdin.readline

d={}
n=int(input())

for _ in range(n):
    name,el=map(str,input().strip().split(" "))

    if el=='enter': el=1
    else: el=0

    if name in d.keys():
        d[name]=el

    else:
        d[name]=el
    

names=list(d.keys())
names.sort(reverse=True)

for name in names:
    if(d[name]==1):
        print(name)
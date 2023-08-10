import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
if m!=0: m_list=list(map(int,input().split()))
else: m_list=[]

default=100
#1000001
minChDiff=sys.maxsize
for ch in range(1000001):
    b=1
    for i in str(ch):
        if int(i) in m_list:
            b=0
            break

    if not b: continue

    if abs(n-ch) < minChDiff: 
        minChDiff=abs(n-ch)
        minCh=ch

res=min(abs(default-n),minChDiff+len(str(minCh)))
print(minChDiff,len(str(minCh)))
print(minCh)

print(res)





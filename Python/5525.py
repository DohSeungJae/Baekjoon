import sys
input=sys.stdin.readline

n=int(input())

cnt=0
pn="IOI"
m=int(input())
s=input().strip()
cur=0
res=0

while cur<m-1:
    if s[cur:cur+3]=="IOI":
        cnt+=1
        cur+=2
        if cnt==n:
            res+=1
            cnt-=1
    else:
        cnt=0
        cur+=1
        


print(res)

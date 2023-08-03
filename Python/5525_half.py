import sys
input=sys.stdin.readline

n=int(input())

cnt=0
pn=""
for i in range(2*n+1):
    if(i%2==0):
        pn+="I"
    else:
        pn+="O"

m=int(input())
s=input().strip()

for i in range(m-(2*n+1)+1):
    if(s[i]=="O"):
        continue
    else:
        if(s[i:i+(2*n)+1]==pn):
            cnt+=1
        
print(cnt)



import sys
input=sys.stdin.readline

a,b=map(int,input().split())

cnt=1
while a<b:
    if(str(b)[-1]=='1'):
        b=b//10
        
    elif(b%2==0):
        b=b//2
    
    else:
        break
  
    cnt+=1

if(a==b):
    print(cnt)
else:
    print(-1)



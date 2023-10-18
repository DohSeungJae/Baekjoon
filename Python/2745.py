import sys
input=sys.stdin.readline

n,b=map(str,input().strip().split())
b=int(b)
res=0
for i in range(len(n)):
    string=n[-(i+1)]
    if string.isdigit():
        res+=int(string)*(b**i)
    else:
        res+=(ord(string)-55)*(b**i)
        
print(res%1000000001)



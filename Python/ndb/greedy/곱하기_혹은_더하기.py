import sys
input=sys.stdin.readline

s=input().strip()

result=int(s[0])
for i in range(1,len(s)):
    n=int(s[i])
    add=result+n
    mul=result*n
    if(add>mul):
        result=add
    else:
        result=mul

print(result)




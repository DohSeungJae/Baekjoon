import sys

input=sys.stdin.readline

s=int(input())

n=1
while(1):
    s1=(n*(n+1))/2
    s2=((n+1)*(n+2))/2

    if(s1 <= s < s2):
        print(n)
        break

    n+=1
    continue

import sys
input=sys.stdin.readline

n=int(input())
cnt5=n%2
while True:
    if(5*(cnt5+2)<=n):
        cnt5+=2
    else:
        break

rest=n-(cnt5*5)
if(n<4 and n!=2):
    print(-1)
    exit(0)

print(cnt5+rest//2)
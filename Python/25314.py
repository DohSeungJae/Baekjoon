import sys
input=sys.stdin.readline

n=int(input())

string="long "
res=""
n=int(n/4)


for _ in range(n):
    res+=string


print(res+"int")

import sys
import math
input=sys.stdin.readline

n=int(input())
l=[]

for i in range(31):
    l.append(i**i)

if n in l:
    print(1)
else:
    print(0)
    
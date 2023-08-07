import sys
input=sys.stdin.readline

part=0
summ=0
x=int(input())

i=1
while summ<x:
    summ+=i
    i+=1
    part+=1
    

s=summ-x+1
m=part-s+1

if(part%2==0):
    s,m=m,s

print(f"{s}/{m}")


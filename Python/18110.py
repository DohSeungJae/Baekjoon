import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
n_list=[]


def rnd(num):
    if num-int(num)>=0.5:
        num=int(num)+1
    else:
        num=int(num)
    
    return num


if(n==0):
    print(0)
    exit(0)

for _ in range(n):
    n_list.append(int(input()))

n_list.sort()

d=deque(n_list)


cut=rnd(n*0.15)

for _ in range(cut):
    d.popleft()
    d.pop()


avg=rnd(sum(d)/len(d))

print(d)

print(avg)

    
        


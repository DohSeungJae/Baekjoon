#1744
import sys

input=sys.stdin.readline

n=int(input())
n_list=[]
p_list=[]

res=[]

def cal(arr):
    while arr:
        n=arr.pop()
        if(arr): res.append(n*arr.pop())
        else: res.append(n)

for _ in range(n):
    num=int(input())
    if num<=0:
        n_list.append(num)
    elif num==1:
        res.append(1)

    else:
        p_list.append(num)

p_list.sort()
n_list.sort(reverse=True)

cal(n_list)
cal(p_list)


print(sum(res))


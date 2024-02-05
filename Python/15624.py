import sys
input=sys.stdin.readline
list=[0,1,1]
n=int(input())

if n<3:
    print(list[n])
else:
    for i in range(3,n+1):
        list.append((list[i-1]+list[i-2])%1000000007)    
    print(list[-1])
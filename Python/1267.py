import sys
input=sys.stdin.readline

n=int(input())
n_list=list(map(int,input().split()))

y=0
m=0

for i in n_list:
    m+=15*(i//60+1)
    y+=10*(i//30+1)


if(m<y):
    print("M",end=" ")
    print(m)
elif(y<m):
    print("Y",end=" ")
    print(y)
else:
    print("Y M ",end="")
    print(m)
    
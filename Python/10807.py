import sys
input=sys.stdin.readline

n=int(input())
i_list=list(map(int,input().split(" ")))
s=int(input())

cnt=0

for i in i_list:
    if(i==s):
        cnt+=1

print(cnt)


import sys
input=sys.stdin.readline

n=int(input())
array=list(map(int,input().split()))

array.sort()

group=0
cnt=0
for i in array:
    cnt+=1
    if(cnt>=i):
        cnt=0
        group+=1

print(group)


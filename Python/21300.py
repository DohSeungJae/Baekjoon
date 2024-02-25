import sys
input=sys.stdin.readline

line=list(map(int,input().split()))
res=0

for i in range(len(line)):
    res+=line[i]
print(res*5)


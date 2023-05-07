#2212
import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
s_list=list(map(int,input().split(" ")))
dis=[]

s_list.sort()

for i in range(len(s_list)-1):
    dis.append(s_list[i+1]-s_list[i])


for _ in range(k-1):
    dis.pop(dis.index(max(dis)))

print(sum(dis))
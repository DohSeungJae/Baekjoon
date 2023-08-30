import sys
input=sys.stdin.readline

list_horses=[1,1,2,2,2,8]

input_horses=list(map(int,input().split()))

for i in range(6):
    print(list_horses[i]-input_horses[i],end=" ")
    
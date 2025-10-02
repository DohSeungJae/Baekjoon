import sys
input=sys.stdin.readline

n=int(input())
array=list(map(int,input().split()))

array.sort(reverse=True)

cnt=0
while len(array)>0:
    fear=array.pop(0)
    if(len(array)>=(fear-1)):
        for _ in range(fear-1):
            array.pop()
        cnt+=1

print(cnt)

#너무 복잡함..


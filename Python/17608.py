import sys
input=sys.stdin.readline

N=int(input())
stack=[]
cnt=0

for _ in range(N):
    stack.append(int(input()))

temp=0
while len(stack)>0:
    popped=stack.pop()
    if(popped>temp):
        temp=popped
        cnt+=1

print(cnt)
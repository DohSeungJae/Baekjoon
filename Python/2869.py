import sys
input=sys.stdin.readline

a,b,v=map(int,input().split())

n1=v-a
n2=a-b

result=n1//n2+int(n1%n2!=0)+1
print(result)

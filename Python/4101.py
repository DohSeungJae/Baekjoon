import sys
input=sys.stdin.readline

n=-1
m=-1

while(n!=0 and m!=0):
    n,m=map(int,input().split())
    if(n>m): print("Yes")
    elif(n==0 and m==0): break
    else: print("No")


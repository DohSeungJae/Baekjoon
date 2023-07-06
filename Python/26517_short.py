import sys
input=sys.stdin.readline

k=int(input())
a,b,c,d=map(int,input().split())
print(f"Yes {r}" if (r:=a*k+b)==c*k+d else "No")

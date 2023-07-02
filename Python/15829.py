import sys
input=sys.stdin.readline
m=1234567891
r=31


l=int(input())
string=input().strip()

h=0
for i in range(l):
    h=h+((ord(string[i])-96)*(31**i))

print(h%m)



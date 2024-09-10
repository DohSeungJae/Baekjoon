import sys
input=sys.stdin.readline

T=int(input())
A=T//300
T-=(T//300)*300

B=T//60
T-=(T//60)*60

C=T//10
T-=(T//10)*10

if(T!=0):
    print(-1)
    exit(0)
else:
    print(A,B,C)

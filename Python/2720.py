import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    C=int(input())
    print(C//25,end=" ")
    C-=(C//25)*25

    print(C//10,end=" ")
    C-=(C//10)*10

    print(C//5,end=" ")
    C-=(C//5)*5

    print(C)
    

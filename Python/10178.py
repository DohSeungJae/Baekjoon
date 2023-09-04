import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    c,v=map(int,input().split())
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(c//v,c%v))
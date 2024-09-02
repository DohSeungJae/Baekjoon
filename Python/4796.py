import sys
input=sys.stdin.readline

i=1
while 1: 
    L,P,V=map(int,input().split())
    if(L==P==V==0):
        break
    seq=V//P
    rest=V%P
    if(rest>=L):
        seq+=1
        rest=0

    ans=seq*L+rest
    print(f'Case {i}: {ans}')
    i+=1

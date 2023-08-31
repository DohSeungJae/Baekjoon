import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())

def powerDAC(a,b):
    
    if(b==1):
        return a%c

    elif(b%2==0):
        temp=powerDAC(a,b//2)
        return (temp*temp)%c 
    else:
        temp=powerDAC(a,b//2)
        return (temp*temp*a)%c

print(powerDAC(a,b))

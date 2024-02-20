import sys
input=sys.stdin.readline

x=int(input())
m=int(input())

def extendedGcd(a,b):
    if(a==0):
        return b,0,1
    gcd,x,y=extendedGcd(b%a,a)
    return gcd,y-(b//a)*x,x

def modInverse(a,m):
    gcd,x,_=extendedGcd(a,m)
    if(gcd!=1):
        return "No such integer exists."
    else:
        return x%m

print(modInverse(x,m))

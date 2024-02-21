import sys
import math
input=sys.stdin.readline


def power(x, y, p):
    # x^y를 p로 나눈 나머지를 계산합니다.
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def modInverseFermat(a, p):
    return power(a, p-2, p)


def extendedGcd(a,b):
    if(a==0):
        return b,0,1
    gcd,x,y=extendedGcd(b%a,a)
    return gcd,y-(b//a)*x,x

def modInverseEuclidean(a,m):
    gcd,x,_=extendedGcd(a,m)
    if(gcd!=1):
        return "No such integer exists."
    else:
        return x%m
    
M=int(input())
res=0
for _ in range(M):
    N,S=map(int,input().split())
    gcd=math.gcd(N,S)
    N//=gcd
    S//=gcd 

    E=(S*modInverseEuclidean(N,(10**9)+7)%((10**9)+7))
    res=(res+E)%((10**9)+7)

print(res)





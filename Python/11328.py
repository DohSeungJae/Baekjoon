rng=(ord('z')-ord('a')+1)
n=int(input())

for _ in range(n):
    a,b=map(str,input().split())
    cnta=[0]*rng
    cntb=[0]*rng

    for c in a:
        cnta[ord(c)-ord('a')]+=1
    for c in b:
        cntb[ord(c)-ord('a')]+=1
    
    able=True
    for i in range(rng):
        if(cnta[i]!=cntb[i]):
            able=False

    if(able): print("Possible") 
    else: print("Impossible")           
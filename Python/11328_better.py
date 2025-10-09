rng=ord('z')-ord('a')+1

n=int(input())

for _ in range(n):
    a,b=map(str,input().split())
    cnt=[0]*rng

    for c in a: cnt[ord(c)-ord('a')]+=1
    for c in b: cnt[ord(c)-ord('a')]-=1

    able=True
    for n in cnt:
        if(n!=0):
            able=False
            break
    
    if(able):print("Possible")
    else:print("Impossible")
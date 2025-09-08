import sys
input=sys.stdin.readline

N=int(input())

threeCount=0
for t in range(N+1):
    for m in range(60):
        for s in range(60):
            if("3" in str(s) or "3" in str(m) or "3" in str(t)):
                threeCount+=1
                
print(threeCount)

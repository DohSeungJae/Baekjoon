import sys
input=sys.stdin.readline

stack=list(input().strip())
explosion=input().strip()[::-1]
stackTemp=[]
temp=''
explosionLen=len(explosion)

while stack: 
    stackTemp.append(stack.pop())
    if(len(stackTemp)<explosionLen):
        continue
    isSame=1
    for i in range(1,explosionLen+1):
        if(stackTemp[-i]!=explosion[-i]):
            isSame=0
            break
    if(isSame):
        for _ in range(explosionLen):
            stackTemp.pop()

if(not len(stackTemp)):
    print("FRULA")
    exit(0)

while stackTemp:
    print(stackTemp.pop(),end="")
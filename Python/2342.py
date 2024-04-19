import sys
input=sys.stdin.readline

commands=list(map(int,input().split()))
foots=[0,0]
totalCost=0

def getCost(foot:int,target:int)->int:
    if(foot==target):
        return 1
    elif(foot==0):
        return 2
    if(abs(foot-target)==2):
        return 4
    return 3

for target in commands:
    if(target==0):
        break
    leftCost=getCost(foots[0],target)
    rightCost=getCost(foots[1],target)
    if(rightCost<=leftCost and foots[0]!=target):
        totalCost+=rightCost
        foots[1]=target
    elif(leftCost<rightCost and foots[1]!=target):
        totalCost+=leftCost
        foots[0]=target

    print(foots)

print(totalCost)




    
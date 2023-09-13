import sys
input=sys.stdin.readline

table=[]
n=int(input())

lineMax=[0 for i in range(3)]
lineMin=[0 for i in range(3)]

for i in range(n):
    l,m,r=map(int,input().split())
    tempMax=[0,0,0]
    tempMin=[sys.maxsize,sys.maxsize,sys.maxsize]
    for j in range(3):
        if(j==0):
            tempMax[0]=max(tempMax[0],lineMax[j]+l)
            tempMax[1]=max(tempMax[1],lineMax[j]+m)

            tempMin[0]=min(tempMin[0],lineMin[j]+l)
            tempMin[1]=min(tempMin[1],lineMin[j]+m)
        elif(j==1):
            tempMax[0]=max(tempMax[0],lineMax[j]+l)
            tempMax[1]=max(tempMax[1],lineMax[j]+m)
            tempMax[2]=max(tempMax[2],lineMax[j]+r)

            tempMin[0]=min(tempMin[0],lineMin[j]+l)
            tempMin[1]=min(tempMin[1],lineMin[j]+m)
            tempMin[2]=min(tempMin[2],lineMin[j]+r)

        else:
            tempMax[1]=max(tempMax[1],lineMax[j]+m)
            tempMax[2]=max(tempMax[2],lineMax[j]+r)

            tempMin[1]=min(tempMin[1],lineMin[j]+m)
            tempMin[2]=min(tempMin[2],lineMin[j]+r)

    lineMax=[tempMax[i] for i in range(3)]
    lineMin=[tempMin[i] for i in range(3)]

print(max(lineMax),min(lineMin))




            

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

#table 정보를 저장하는 2차원 리스트를 한번에 입력받을 경우 메모리 초과가 발생함.
#for 반복문을 실행할 때 한 줄의 데이터(3개 값)를 저장할 수 있는 임시 공간 l,m,r
#3개의 변수를 for 반복문이 실행될 때마다 초기화하기 때문에 
#table의 정보 전체를 입력받는 방식모다 메모리를 훨씬 적게 사용함.

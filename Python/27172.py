import sys
input=sys.stdin.readline

size=1000001
n=int(input())
numList=list(map(int,input().split()))
res=[0]*size
isCard=[0]*size
for i in numList:
    isCard[i]=1
    
for i in numList:
    for j in range(i*2,size,i):
        if(isCard[j]):
            res[i]+=1
            res[j]-=1

 
for i in numList:
    print(res[i],end=" ")

#메모리 제한이 높기 때문에 전체 범위 크기를 가지는
#res배열,isCard 배열을 선언
#res는 점수값, isCard는 어떤 카드가 존재하는지 판단하는 배열임.

### 배수로 for 반복문을 순회할 때
### for 반복문 안에서 step을 따로 설정하는 것이
### 변수를 선언하여 값을 곱하는 방식보다 시간이 훨씬 빠름
### range() 내부에서 실행하는 것이 더 빠르기 때문??
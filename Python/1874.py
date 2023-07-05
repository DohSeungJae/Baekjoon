import sys
input=sys.stdin.readline
n=int(input())

cnt=0
res=[]
stack=[]

while len(res)!=2*n:
    num=int(input())
    
    if(num>cnt):
        while(num!=cnt):
            res.append("+")
            cnt+=1
            stack.append(cnt)
  
        res.append("-")
        stack.pop()

    elif(num<cnt):

        if(stack.pop()==num):
            res.append("-")

        else:
            print("NO")
            sys.exit(0)


for i in res:
    print(i)

        
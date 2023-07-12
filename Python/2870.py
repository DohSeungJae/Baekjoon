import sys
input=sys.stdin.readline

n=int(input())
res=[]

for _ in range(n):
    string=str(input()).strip()
    
    number=""
    for i in string:
        if(i.isdigit()):
            number+=i
        else:
            if len(number)!=0:
                res.append(int(number))
                number=""

    if(number.isdigit()):
        res.append(int(number))
        number=""



res.sort()
for i in res:
    print(i)
    




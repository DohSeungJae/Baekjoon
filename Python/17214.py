import sys
input=sys.stdin.readline

eq="" #result equation
op="+"
string=str(input().strip())

if string[0]=='-': 
    string=string[1:]
    eq+="-"

if "-" in string: op="-"

rands=list(map(str,string.split(op)))

if '0' in rands:
    rands.remove("0")

for j in range(len(rands)):
    rand=rands[j]

    num="" #rand에서 숫자만 가져옴
    for i in rand:
        if i.isdigit():
            num+=i

    if 'x' in rand: #일차식인 경우
        num=int(int(num)/2)
        if num!=1: eq+=str(num)
    
        eq+="xx"

    else: ##상수인 경우
        if(num=="0"): break
        elif(num!="1"): eq+=num
        eq+='x'

    if(len(rands)-1!=j and num!="0"):
     
        eq+=op

if(len(rands)==0):
    print(eq+"W")
else:
    print(eq+"+W")
#다항 함수의 적분

import sys
input=sys.stdin.readline

pss=input().strip()
stack=[]

total=0
temp=1
isAddition=0
for i in pss:
    if(i=='(' or i=='['):
        stack.append(i)
        isAddition=1
        if(i=='('):
            temp*=2
        else:
            temp*=3
    else:
        if(not len(stack)>0):
            total=0
            break
        elif(i==')'):
            if(stack.pop()!='('):
                total=0
                break
        elif(i==']'):
            if(stack.pop()!='['):
                total=0
                break
        if(isAddition):
            total+=temp
            isAddition=0
        if(i==')'):
            temp//=2
        else:
            temp//=3

if(len(stack)>0):
    total=0

print(total)
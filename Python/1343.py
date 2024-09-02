import sys
input=sys.stdin.readline

line=input().strip()+'.'
spaceSeq=1
res=[]

for i in range(len(line)-1):
    if(line[i]!="." and line[i+1]=='.'):
        if(spaceSeq%2!=0):
            print(-1)
            exit(0)
        for j in range((spaceSeq//4)*4):
            res.append("A")
        for j in range(spaceSeq%4):
            res.append("B")
        spaceSeq=1
    elif(line[i]=="." and i!=len(line)):
        res.append(".")
    else:
        spaceSeq+=1

for i in res:
    print(i,end="")
print()

        


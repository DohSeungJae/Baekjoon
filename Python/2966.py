import sys
input=sys.stdin.readline

N=int(input())
answer=input().strip()

A=["A","B","C"]
B=["B","A","B","C"]
G=["C","C","A","A","B","B"]

Adrian=0
Bruno=0
Goran=0

for i in range(N):
    c=answer[i]
    Adrian+=int(A[i%3]==c)
    Bruno+=int(B[i%4]==c)
    Goran+=int(G[i%6]==c)

maxScore=max(Adrian,Bruno,Goran)
print(maxScore)
if(Adrian-maxScore>=0):
    print("Adrian")
if(Bruno-maxScore>=0):
    print("Bruno")
if(Goran-maxScore>=0):
    print("Goran")


import sys
input=sys.stdin.readline

N=int(input())
wordList=[]
totalSum=0

for _ in range(N):
    wordList.append(input().strip())

weightOfChar={}
for word in wordList:
    wordR=word[::-1]
    for i in range(len(word)):
        char=wordR[i]
        if(char not in weightOfChar.keys()):
            weightOfChar[char]=0
        weightOfChar[char]+=int("1"+"0"*i)

charToValue={i:0 for i in weightOfChar.keys()}
value=9

for _ in range(len(weightOfChar.keys())):
    maxWeight=0
    highestChar=""
    for k,v in weightOfChar.items():
        if(k.isdigit()):
            continue
        if(v>maxWeight):
            highestChar=k
            maxWeight=v
    
    charToValue[highestChar]=str(value)
    value-=1
    del weightOfChar[highestChar]
    
for i in range(len(wordList)):
    for j in range(len(wordList[i])):
        char=wordList[i][j]
        if(char.isdigit()):
            continue
        wordList[i]=wordList[i].replace(char,charToValue[char])

for digit in wordList:
    totalSum+=int(digit)
    
print(totalSum)
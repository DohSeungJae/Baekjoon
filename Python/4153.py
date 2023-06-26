import sys
input=sys.stdin.readline

while(True):
    t=list(map(int,input().split(" ")))
    if(t[0]==t[1]==t[2]==0):
        break
    
    t.sort()
    
    if(t.pop()**2==t.pop()**2+t.pop()**2):
        print("right")
    else:
        print("wrong")
    
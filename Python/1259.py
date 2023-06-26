import sys
input=sys.stdin.readline


while(True):
    string=str(input()).strip()
    string=str(int(string))
    if(string=="0"):
        break

    j="yes"

    for i in range(int(len(string)/2)):
        if(string[i]==string[len(string)-1-i]):
            continue
        else:
            j="no"
    
    print(j)




    
    
    
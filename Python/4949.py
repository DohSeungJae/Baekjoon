import sys
input=sys.stdin.readline


string=""
while(True):
    string=input().rstrip()


    stack=[]
    res="yes"


    if(string=="."):
        break

    for i in string:


        if(i=="(" or i=="["):
            stack.append(i)
        
        if(i==")"):
            if(len(stack)==0): 
                res="no"
                
            elif(stack.pop()!="("):
                res="no"
    
        if(i=="]"):
            if(len(stack)==0):
                res="no"

            elif(stack.pop()!="["):
                res="no"
    
    if(len(stack)!=0):
        res="no"

    print(res)


        

        
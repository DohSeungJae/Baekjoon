import sys
input=sys.stdin.readline

n,y,x=map(int,input().split())

std_x=0
std_y=0
value=0

while n>0:

    shift=2**(n-1)
    if(std_x<=x<std_x+shift and std_y<=y<std_y+shift): #I
        n-=1

    elif(std_x+shift<=x<std_x+(2*shift) and std_y<=y<std_y+shift): #II   
        std_x+=shift
        value+=(2**(2*(n-1)))*1
        n-=1        

    elif(std_x<=x<std_x+shift and std_y+shift <=y<std_y+(2*shift)): #III
        std_y+=shift
        value+=(2**(2*(n-1)))*2
        n-=1

    else : # IV  
        std_x+=shift
        std_y+=shift
        value+=(2**(2*(n-1)))*3
        n-=1


print(value)

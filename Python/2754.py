import sys
input=sys.stdin.readline

grades={"A0":4.0,"B0":3.0,"C0":2.0,"D0":1.0}

grade=input().strip()
if(grade=="F"):
    print("0.0")
    exit(0)

if(grade[1]=="0"):
    print(grades[grade])
elif(grade[1]=="+"):
    print(grades[grade.replace("+","0")]+0.3)
elif(grade[1]=="-"):
    print(grades[grade.replace("-","0")]-0.3)
import sys
input=sys.stdin.readline

N=int(input())

grades=[]
for _ in range(N):
    name, grade=input().strip().split()
    grades.append((name,int(grade)))


grades.sort(key=lambda x:x[1])
for grade in grades:
    print(grade[0],end=" ")




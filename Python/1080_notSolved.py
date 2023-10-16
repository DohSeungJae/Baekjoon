import sys
input=sys.stdin.readline

n,m=map(int,input().split())

mat1=[]
mat2=[]

def mat(n,mat):
    for i in range(n):
        line=str(input().strip())
        l_temp=[]
        for i in line:
            l_temp.append(int(i))
        mat.append(l_temp)

            
mat(n,mat1)
mat(n,mat2)

    

print(mat1)
print(mat2)


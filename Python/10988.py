a=input()

isPalin=1

for i in range(len(a)//2):
    if a[i]!=a[-(i+1)]:
        isPalin=0
        break

print(isPalin)
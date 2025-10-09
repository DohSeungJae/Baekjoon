rng=ord('z')-ord('a')+1
diff=[0]*rng

a=input()
b=input()

for c in a: diff[ord(c)-ord('a')]+=1
for c in b: diff[ord(c)-ord('a')]-=1

for i in range(rng):
    if(diff[i]<0):
        diff[i]=diff[i]*(-1)
'''
for i in range(rng): diff[i]=abs(diff[i])
내장함수 쓰는 방식, 
가독성이 조금 더 좋지만
속도는 약간 더 느린 것 같기도?
'''
print(sum(diff))
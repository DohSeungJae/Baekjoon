string=input()
cnt=[0]*26 #a부터 z까지

for c in string:
    '''
    idx=ord(c)-ord('a')
    cnt[idx]+=1
    내가 작성한 코드
    '''

    #더 간단한 코드
    cnt[ord(c)-97]+=1
    

for n in cnt:
    print(n,end=" ")

#try : 1
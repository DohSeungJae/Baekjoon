import queue
import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    n_list=list(map(int,input().split()))
    q=queue.Queue()
    cnt=0

    for i in n_list:
        q.put(i)
    
    bFinish=False
    while((not q.empty()) and not bFinish):
        i=q.get()

        if(i!=max(n_list)):
            q.put(i)
            if(m==0):
                m=len(n_list)-1
            else:
                m-=1        
        else:
            cnt+=1
            if(m==0):
                n_list.remove(i)
                print(cnt)
                bFinish=True
            else:
                m-=1
                n_list.remove(max(n_list))


                
        


        

    

    



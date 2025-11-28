import math
for _ in range(int(input())):
    num=int(input())
    print("1",end="")
    for i in range(2,int(math.sqrt(num))+1):
        cnt=0
        while(num%i==0): 
            cnt+=1
            num/=i
        if cnt!=0: 
            print(" * ",end='')
            print(i,"^",cnt,sep='',end='')
    if(num>1):       
        print(" * ",end='')
        print(int(num),"^","1",sep='')  
    print()
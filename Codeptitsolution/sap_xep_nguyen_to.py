import math
nt=[1]*1000001
nt[0]=nt[1]=0
def sang():
    for i in range (2,int(math.sqrt(1000001))):
        if nt[i]==1:
            for j in range (i*i,1000001,i):
                nt[j]=0


if __name__ == '__main__':
    sang()
    n=int(input())
    a=list(map(int,input().split()))
    
    b=sorted([x for x in a if nt[x]==1])
    j=0
    for i in a:
        if nt[i]==1:
            print(b[j],end=" ")
            j+=1
        else: print(i,end=" ")
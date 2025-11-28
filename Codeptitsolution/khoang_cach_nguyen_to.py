import math

nt=[1]*10001
nt[0]=nt[1]=0
arr=[]
def sang():
    for i in range (2,int(math.sqrt(10001*10001))):
        if nt[i]==1:
            arr.append(i)
            for j in range (i*i,10001,i):
                nt[j]=0

if __name__ == '__main__':
    sang()
    n,a=map(int,input().split())
    print(a,end=" ")
    for i in range(n):
        a+=arr[i]
        print(a,end=" ")
    print(10001*10001)
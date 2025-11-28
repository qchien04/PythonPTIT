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
    t=int(input())
    for _ in range(t):
        count=0
        num=int(input())
        for i in range(1,num):
            if math.gcd(i,num)==1:
                count=count+1
        print('YES') if nt[count]==1 else print('NO')
import math

nt=[1]*1000001
nt[0]=nt[1]=0
def sang():
    for i in range (2,int(math.sqrt(1000001))):
        if nt[i]==1:
            for j in range (i*i,1000001,i):
                nt[j]=0

if __name__ == '__main__':
    n,m=map(int,input().split())
    for i in range(n,m-1):
        for j in range(i+1,m):
            for k in range(j+1,m+1):
                if math.gcd(i,j)==1 and math.gcd(k,j)==1 and math.gcd(k,i)==1 :
                    print("(",i,", ",j,", ",k,")",sep="")
import math

nt=[1]*1000001
nt[0]=nt[1]=0
def sang():
    for i in range (2,int(math.sqrt(1000001))):
        if nt[i]==1:
            for j in range (i*i,1000001,i):
                nt[j]=0

def dk2(n):
    s1=str(n)
    s2=s1[::-1]
    return s1!=s2 and nt[int(s2)]>=1

    

if __name__ == '__main__':
    sang()
    t=int(input())
    for _ in range(t):
        num=int(input())
        for i in range(num):
            if nt[i]==1 and dk2(i)==True:
                if(int(str(i)[::-1])<num):
                    print(i,end=" ")
                    print(str(i)[::-1],end=" ")
                    nt[int(str(i)[::-1])]=2
        print()
import math

nt=[1]*1000001
nt[0]=nt[1]=0
def sang():
    for i in range (2,int(math.sqrt(1000001))):
        if nt[i]==1:
            for j in range (i*i,1000001,i):
                nt[j]=0

def solve(a,b):
    gcd=list(map(int,str(math.gcd(a,b))))
    if nt[sum(gcd)]==1 : return True
    else: return False
if __name__ == '__main__':
    sang()
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        print('YES') if solve(a,b) else print('NO')
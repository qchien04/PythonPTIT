import math

nt=[1]*1000001
nt[0]=nt[1]=0
def sang():
    for i in range (2,int(math.sqrt(1000001))):
        if nt[i]==1:
            for j in range (i*i,1000001,i):
                nt[j]=0
sang()

n,m=map(int,input().split())
a=[]
maxx=-1
check=True
for i in range(n):
    b=list(map(int,input().split()))
    for j in b:
        if nt[j]==1:
            maxx=max(maxx,j)
            check=False
    a.append(b)
if not check:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j]==maxx:
                print(f"Vi tri [{i}][{j}]")
else: print("NOT FOUND")

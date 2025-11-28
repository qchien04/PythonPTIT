import math

nt=[1]*1000001
nt[0]=nt[1]=0
def sang():
    for i in range (2,int(math.sqrt(1000001))):
        if nt[i]==1:
            for j in range (i*i,1000001,i):
                nt[j]=0
sang()
n=int(input())
a=list(map(int,input().split()))
se=set()
b=[]
sum=0
for i in a:
    if i not in se:
        se.add(i)
        b.append(i)
        sum+=i
c_sum=0
check=True
for i in range(len(b)):
    c_sum+=b[i]
    sum-=b[i]
    if nt[c_sum]==1 and nt[sum]==1:
        check=False
        print(i)
        break
if check: print("NOT FOUND")

import math

nt=[1]*100001
nt[0]=nt[1]=0
primes=[]
def sang():
    for i in range (2,100001):
        if nt[i]==1:
            for j in range (i*i,100001,i):
                nt[j]=0
    for i in range(10001):
        if nt[i]==1: primes.append(i)
sang()
n=int(input())
a=list(map(int,input().split()))
a.sort()
cnt=0
chot=0
for i in a:
    if nt[i]==1:continue
    j=chot
    while i>primes[j]:
        j+=1
    chot=j-1
    cnt=max(cnt,min(i-primes[chot],primes[j]-i))
print(cnt)
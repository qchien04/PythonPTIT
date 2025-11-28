
n=int(input())
a=list(map(int,input().split()))

buoc=9999999
choose=0

for i in a:
    tmp=0
    for j in a:
        tmp+=abs(i-j)
    if tmp<buoc:
        buoc=tmp
        choose=i
print(buoc,choose)

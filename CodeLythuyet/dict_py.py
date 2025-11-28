from collections import Counter
arr=[]
num=int(input())
arr=list(map(int,input().split()))
lis=dict(Counter(arr))
cus=int(input())
benerfit=0
for i in range(0,cus):
    inp=list(map(int,input().split()))
    if inp[0] in lis:
        if lis[inp[0]]>0:
            benerfit+=inp[1]
            lis[inp[0]]=lis[inp[0]]-1
print(benerfit)
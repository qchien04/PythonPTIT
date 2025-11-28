from collections import Counter
s=input()
arr=[]
n=int(input())
a=0
if len(s)%2==0:
    a=len(s)
else: a=len(s)-1
for i in range(0,a-1,2):
    arr.append(int(s[i:i+2]))   
lis=Counter(arr)
check=True
lis=sorted([[key,val] for key,val in lis.items()],key=lambda x:x[0])

for i in lis:
    if i[1]>=n:
        check=False
        print(i[0],i[1])
if check: print("NOT FOUND")
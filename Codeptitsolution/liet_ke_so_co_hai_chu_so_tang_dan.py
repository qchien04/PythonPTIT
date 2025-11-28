from collections import Counter

s=input()
arr=[]
a=0
if len(s)%2==0:
    a=len(s)
else: a=len(s)-1
for i in range(0,a-1,2):
    arr.append(int(s[i:i+2]))   
lis=Counter(arr)

lis=sorted([key for key in lis.keys()],key=lambda x:x)

for i in lis:
    print(i,end=" ")
from collections import OrderedDict
s=input()
arr=OrderedDict()
a=0
if len(s)%2==0:
    a=len(s)
else: a=len(s)-1
for i in range(0,a-1,2):
    num=int(s[i:i+2])
    if num not in arr:
        arr[num]=1
    else:
        arr[num]+=1  
lis=[[key,val] for key,val in arr.items()]

for i in lis:
    print(i[0],i[1])
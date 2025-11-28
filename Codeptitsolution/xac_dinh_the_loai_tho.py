n=int(input())
a=[]
for _ in range(n):
    a.append(input())
truoc=-1
i=0
ans=[]
while(i<n):
    b=a[i].split()
    if(len(b)==7):
        truoc=-1
        ans.append(2)
        i+=4
    elif(len(b)==6):
        if(truoc==-1):
            truoc=1
            ans.append(1)
        i+=2
print(len(ans))
for j in ans:
    print(j)




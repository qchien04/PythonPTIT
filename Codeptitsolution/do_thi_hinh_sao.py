
n=int(input())
bac=[0]*(n+1)
if(n==1): print("Yes")
else:
    for i in range(n-1):
        a,b=map(int,input().split())
        bac[a]+=1
        bac[b]+=1
    x=0
    y=0
    for i in range(1,n+1):
        if bac[i]==n-1:
            x+=1
        elif bac[i]==1:
            y+=1
    if x==1 and y==n-1:
        print("Yes")
    else: print("No")


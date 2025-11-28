
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    ans=[]
    i=j=l=0
    while i<len(a) and j<len(b) and l<len(c):
        if a[i]==b[j]==c[l]: 
            ans.append(a[i])
            i+=1
            j+=1
            l+=1
        elif b[j]<a[i]:
            j+=1
        elif c[l]<a[i]:
            l+=1;
        else: i+=1
    for i in ans:
        print(i,end=" ")
    if len(ans)==0: print("NO",end=" ")
    print()

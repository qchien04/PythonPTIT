for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))

    res=[]
    i=0
    j=0
    h=0
    while i<n and j<m and h<k:
        if a[i]==b[j]==c[h]:
            res.append(a[i])
            i+=1
            j+=1
            h+=1
        elif a[i]<b[j]:
            i+=1
        elif b[j]<c[h]:
            j+=1
        else: h+=1
    if len(res)==0:print("NO")
    else:
        for i in res:
            print(i,end=" ")
    print()
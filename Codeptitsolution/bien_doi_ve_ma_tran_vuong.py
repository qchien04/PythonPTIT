n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
if n>m:
    l=(n-m)*2
    for i in range(n):
        if i<l and i%2==0:
            continue
        for j in range(m):
            print(a[i][j],end=" ")
        print()
elif n<m:
    l=1+(m-n)*2
    for i in range(n):
        for j in range(m):
            if j<l and j%2==1:
                continue
            print(a[i][j],end=" ")
        print()
else:
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=" ")
        print()

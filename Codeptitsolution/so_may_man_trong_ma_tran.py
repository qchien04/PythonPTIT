n,m=map(int,input().split())
a=[]
maxx=-1
minn=9999999
check=True
for i in range(n):
    b=list(map(int,input().split()))
    maxx=max(max(b),maxx)
    minn=min(min(b),minn)
    a.append(b)
for i in range(n):
    for j in range(m):
        if a[i][j]==(maxx-minn):
            check=False
            break
if not check:
    print(maxx-minn)
    for i in range(n):
        for j in range(m):
            if a[i][j]==(maxx-minn):
                print(f"Vi tri [{i}][{j}]")
else: print("NOT FOUND")

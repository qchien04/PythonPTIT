n,m=map(int,input().split())
a=[]
maxx=-1
check=True
for i in range(n):
    b=list(map(int,input().split()))
    for j in b:
        if j>10:
            if str(j)==str(j)[::-1]:
                maxx=max(maxx,j)
                check=False
    a.append(b)
if not check:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j]==maxx:
                print(f"Vi tri [{i}][{j}]")
else: print("NOT FOUND")

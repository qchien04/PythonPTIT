for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[]
    b=[]
    for _ in range(n): a.append(list(map(int,input().split())))
    for _ in range(3): b.append(list(map(int,input().split())))
    ans=[([0]*(m-2)) for _ in range(n-2)]
    for i in range(n):
        if i==n-2: break
        for j in range(m):
            if j==m-2: break
            for k in range(3):
                for l in range(3):
                    ans[i][j]+=b[k][l]*a[i+k][j+l]
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j],end=" ")
        print()
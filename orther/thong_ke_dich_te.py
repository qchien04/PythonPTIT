n,m=map(int,input().split())
res,a=0,[]
for i in range(n): 
    a.append(list(map(int, input().split())))
vs=[[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x==0 and y==0: continue
                    if 0<=x+i and x+i<n and 0<=j+y and j+y<m and vs[i+x][j+y]==0:
                        res+=a[i+x][j+y]
                        vs[i+x][j+y]=1
print(res)
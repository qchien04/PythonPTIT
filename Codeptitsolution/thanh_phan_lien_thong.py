from collections import defaultdict
vs=[0]*301
def dfs(x):
    vs[x]=1
    for i in gr[x]:
        if(vs[i]==0):
            dfs(i)
n,m,x=map(int,input().split())
gr=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    gr[a].append(b)
    gr[b].append(a)
dfs(x)
for i in range(1,n+1):
    if vs[i]==0:
        print(i)

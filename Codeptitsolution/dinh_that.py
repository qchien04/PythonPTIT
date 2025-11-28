
vs=[]
dsk=[]
list_result=[]
def dfs(u,e,arr):
    arr.append(u)
    vs[u]=True
    for i in dsk[u]:
        if vs[i]==False:
            if i==e:
                list_result.append(arr)
            dfs(i,e,arr.copy())
            vs[i]=False


for _ in range(int(input())):
    n,m,u,v=map(int,input().split())
    vs=[False]*(n+1)
    dsk=[[] for i in range(n+1)]
    list_result=[]
    for _ in range(m):
        s,e=map(int,input().split())
        dsk[s].append(e)
    dfs(u,v,[])
    ans=set([i for i in range(1,n+1)])
    for i in list_result:
        ans=ans&(set(i[1:]))
    if len(ans)==n:
        print(0)
    else:print(len(ans))
    
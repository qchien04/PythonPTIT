t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=[]
    while len(a)<n:
        a.extend(list(map(int,input().split())))
    maxindex=a.index(max(a))
    a.insert(maxindex,m)
    am=[i for i in a if i<0]
    duong=[i for i in a if i>=0]
    am.extend(duong)
    for i in am:
        print(i,end=" ")
    print()


for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        b,c=map(int,input().split())
        a.append((b,c))
    a.sort(key=lambda x:(x[1],x[0]))
    ans=1
    end=a[0][1]
    for i in range(1,len(a)):
        if a[i][0]>=end:
            ans+=1
            end=a[i][1]
    print(ans)

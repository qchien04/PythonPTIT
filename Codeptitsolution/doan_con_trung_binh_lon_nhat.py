n=int(input())

a=list(map(int,input().split()))
maxx=max(a)
i=0
ans=1
while i<n:
    if a[i]!=maxx:
        i+=1
        continue
    i+=1
    cnt=1
    while i<n and a[i]==maxx:
        cnt+=1
        i+=1
    ans=max(ans,cnt)
print(ans)

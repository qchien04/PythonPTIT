n=int(input())

for _ in range(n):
    s=input().split()
    l=0
    i=0
    ans=""
    while True and i<len(s):
        if l+len(s[i])<=100:
            ans=ans+s[i]+" "
            l=l+len(s[i])+1
        else: break
        i+=1
    print(ans)

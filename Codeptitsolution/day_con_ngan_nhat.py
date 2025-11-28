import math

for _ in range(int(input())):
    x=list(map(int,input().split()))
    n=0
    k=0
    if len(x)==1:
        n=x[0]
        k=int(input())
    else:
        n=x[0]
        k=x[1]
    arr=[]
    while len(arr)!=n:
        b=list(map(int,input().split()))
        arr+=b
    ans=100000
    for i in range(n):
        c_gcd=0
        for j in range(i,n):
            c_gcd=math.gcd(c_gcd,arr[j])
            if c_gcd==k:
                ans=min(ans,j-i+1)
    print(ans) if ans!=100000 else print("-1")
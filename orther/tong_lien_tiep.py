def cnt(n):
    count=0
    k=2
    while k*(k-1)//2<n:
        if (n-k*(k-1)//2)%k == 0:
            m=(n-k*(k-1)//2)//k
            if m>0:
                count+=1
        k+=1
    return count
for _ in range(int(input())):
    n=int(input())
    print(cnt(n))

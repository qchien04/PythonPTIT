mod = 10**9 + 7
for i in range(int(input())):
    n,k=map(int, input().split())
    a = bin(k)[2:]
    sum = 0
    b = len(a)-1
    for i in a:
        sum=(sum+int(i)*(n**b))%mod
        b -= 1
    print(sum)
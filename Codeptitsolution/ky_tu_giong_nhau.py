t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a, b, c = map(int, input().split())
    lis = [0] * (n + 2)
    lis[1] = a
    
    for i in range(2, n + 1):
        if i % 2 == 0:
            lis[i] = min(lis[i - 1] + a, lis[i // 2] + c)
        else:
            lis[i] = min(lis[i - 1] + a, lis[(i + 1) // 2] + c + b)
    
    print(lis[n])
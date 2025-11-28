N = int(input())
a = list(map(float, input().split()))

minn= min(a)
maxx= max(a)

b=[d for d in a if d != minn and d != maxx]

ans = sum(b)/len(b)

print(f"{ans:.2f}")
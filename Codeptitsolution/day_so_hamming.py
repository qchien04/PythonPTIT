import bisect
a = set()
max = int(1e18)
for i in range(65):
    n2 = 2**i
    if n2 > max: break
    a.add(n2)
    for j in range(40):
        n3 = 3**j
        if n2*n3 > max: break
        a.add(n2*n3)
        for k in range(28):
            n5 = 5**k 
            if n2*n3*n5 > max: break
            a.add(n2*n3*n5)
a = sorted(a)

for t in range(int(input())):
    n=int(input())
    index=bisect.bisect_left(a,n)
    if a[index]==n:
        print(index+1)
    else:print("Not in sequence")
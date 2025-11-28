import math
from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=list(map(int,input().split()))

    all_gcd_in_a=defaultdict(int)
    all_gcd_in_a[0]=0
    for i in range(n):
        b=list(all_gcd_in_a.keys())
        for j in b:
            new_gcd=math.gcd(j,a[i])
            cost=all_gcd_in_a[j]+c[i]
            if new_gcd not in all_gcd_in_a:
                all_gcd_in_a[new_gcd]=cost
            else:
                if cost<all_gcd_in_a[new_gcd]:
                    all_gcd_in_a[new_gcd]=cost
    if 1 not in all_gcd_in_a:
        all_gcd_in_a[1]=-1
    print(all_gcd_in_a[1])

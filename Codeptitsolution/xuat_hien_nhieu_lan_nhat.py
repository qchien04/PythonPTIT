from collections import Counter
for _ in range(int(input())):
    arr=[]
    num=int(input())
    arr=list(map(int,input().split()))
    lis=dict(Counter(arr))
    check=False
    for key,val in lis.items():
        if val>(len(arr)/2):
            check=True
            print(key)
            break
    if not check: print("NO")
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    arr=Counter(list(map(int,input().split())))
    for key,val in arr.items():
        if val%2==1: 
            print(key)
            break

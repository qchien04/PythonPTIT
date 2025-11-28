from collections import Counter
for _ in range(int(input())):
    arr=[]
    num=int(input())
    for i in range(num):
        arr.append(int(input()))


    lis=dict(Counter(arr))
    max_value = max(lis.values())
    bingo=[key for key in lis.keys() if lis[key]==max_value]
    print(min(bingo))
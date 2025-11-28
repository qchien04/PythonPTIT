n=int(input())
a=[]
for _ in range(n):
    b={
        "ma": input(),
        "name":input(),
        "ht":input(),
    }
    a.append(b)
a=sorted(a,key=lambda x: x["ma"])
for i in a:
    print(i["ma"],i["name"],i["ht"])
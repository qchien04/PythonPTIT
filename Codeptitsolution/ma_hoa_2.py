p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
if __name__ == '__main__':
    while True:
        t=input()
        if t=="0":break
        k,s=t.split()
        res=""
        for i in s:
            res+=p[(p.index(i)+int(k))%28]
        print(res[::-1])

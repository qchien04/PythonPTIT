for _ in range(int(input())):
    s=input()
    a=[int(i) for i in s if i.isdigit()]
    for i in sorted(s):
        if i.isalpha():print(i,end="")
    print(sum(a))
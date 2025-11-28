

for _ in range(int(input())):
    a=input()
    s1=a[0:2]
    s2=a[-2:]
    if(s1==s2): print("YES")
    else: print("NO")
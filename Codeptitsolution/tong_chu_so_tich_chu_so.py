for _ in range(int(input())):
    s=input()
    sum=0
    t=1
    check=False
    for i in range(0,len(s)):
        if i%2==1:
            sum+=int(s[i])
        else:
            if s[i]!="0": t*=int(s[i])
            if s[i]!="0":check=True
    print(t,end=" ") if check else print("0",end=" ")
    print(sum)
    



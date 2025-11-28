n=int(input())
i=0
while i<n:
    a=input()
    print(a,end=": ")
    cnt=0
    i+=1
    while True and i<n:
        i+=1
        b=input()
        if b!="":
            cnt+=1
        else:break
    print(cnt)
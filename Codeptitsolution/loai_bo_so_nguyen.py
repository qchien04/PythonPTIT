

ans=[]


with open("DATA.in",'r') as f:
    data=f.readlines()
    lmt=2**31-1
    for i in data:
        b=i.split()
        for j in b:
            try:
                x=int(j)
                if x>lmt:
                    ans.append(j)
            except Exception as e:
                ans.append(j)
    ans.sort()
    for i in ans:print(i,end=" ")
        

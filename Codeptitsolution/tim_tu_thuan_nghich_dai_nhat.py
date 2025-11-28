from collections import OrderedDict
maxx=-1
dic=OrderedDict()

with open("VANBAN.in",'r') as f:
    data=f.readlines()
    for i in data:
        b=i.split()
        for j in b:
            if j==j[::-1]:
                maxx=max(maxx,len(j))
                if j in dic.keys():
                    dic[j]+=1
                else: dic[j]=1
    for key,val in dic.items():
        if len(key)==maxx:
            print(key,val)
        

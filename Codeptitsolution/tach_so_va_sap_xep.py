a=[]
import re
for _ in range(int(input())):
    s=input()
    b=re.findall(r"\d+",s)
    for i in b: a.append(int(i))
a.sort()
for i in a:print(i)
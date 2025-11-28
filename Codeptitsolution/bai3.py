import re
from collections import Counter
t=int(input())
a=[]
for _ in range(t):
    s=re.sub(r'[^A-Za-z0-9]+'," ",input())
    s=re.sub(r'[\d+]','',s)
    a.extend(s.lower().strip().split())
c=Counter(a)
c=sorted(c.items(),key=lambda x:(-x[1],x[0]))
for i in c:
    if re.match(r"[\d+]",i[0]): continue
    print(*i)
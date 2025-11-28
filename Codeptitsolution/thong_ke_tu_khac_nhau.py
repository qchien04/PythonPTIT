import re
from collections import Counter
t=int(input())
a=[]
for _ in range(t):
    s=re.sub(r'[^A-Za-z]'," ",input())
    a.extend(s.lower().strip().split())
c=Counter(a)
c=sorted(c.items(),key=lambda x:(-x[1],x[0]))
for i in c:
    print(*i)
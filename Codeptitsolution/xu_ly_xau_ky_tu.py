def lower1(s):
    return s.lower()
s1=set(map(lower1,input().split()))
s2=set(map(lower1,input().split()))

a=sorted(s1|s2)
b=sorted(s1&s2)

for i in a:
    print(i,end=' ')
print()
for i in b:
    print(i,end=' ')
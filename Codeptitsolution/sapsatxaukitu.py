from collections import Counter

for i in range(int(input())):
    s1=sorted(list(input()))
    s2=sorted(list(input()))
    c1=Counter(s1)
    c2=Counter(s2)
    if len(c1)!=len(c2):
        print(f"Test {i+1}: NO")
        continue
    check=True
    for k in c1.keys():
        if c1[k]!=c2[k]:
            print(f"Test {i+1}: NO")
            check=False
            break
    if check==False: continue
    print(f"Test {i+1}: YES")


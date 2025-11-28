a = set()
def solve(i, s, cnt):
    if i==10: return
    if cnt*2 > i: a.add(int(s))
    for c in "012": 
        solve(i+1, s+c, cnt+1 if c=="2" else cnt)
solve(0,"",0)
a = sorted(a)
for _ in range(int(input())):
    n = int(input())
    for i in range(n): 
        print(a[i], end=" ")
    print()
# a = set()
# def solve(i, s, cnt):
#     if i==10: return
#     if cnt*2 > i: a.add(int(s))
#     for c in "012": 
#         solve(i+1, s+c, cnt+1 if c=="2" else cnt)
# solve(0,"",0)
# a = sorted(a)
# for _ in range(int(input())):
#     n = int(input())
#     for i in range(n): 
#         print(a[i], end=" ")
#     print()

st = set()
def tryAt(s, c2, max_len=10): 
    if c2 != 0 and c2 >= len(s) / 2:
        st.add(int(s))
    if len(st) < 10000 and len(s) < max_len:
        tryAt(s + '0', c2=c2)
        tryAt(s + '1', c2=c2)
        tryAt(s + '2', c2=c2 + 1)

tryAt(s='', c2=0)
li = list(st)
li.sort()
for _ in range(int(input())):
    for i in range(int(input())):
        print(li[i], end=' ')
    print()



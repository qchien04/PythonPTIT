a=['2','3','5','7']
def check(s):
    if len(s)<4: return False
    for i in a:
        if i not in s:
            return False
    if s[-1]=='2': return False
    return True
ans=[]
def solve(s,n):
    if len(s)>=n: return
    if check(s): ans.append(int(s))
    for i in a:
        solve(s+i,n)
n=int(input())
solve('',n+1)
ans.sort()
for i in ans:
    print(i)

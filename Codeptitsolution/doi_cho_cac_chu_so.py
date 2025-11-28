def solve(s):
    n=len(s)
    s=list(s)
    i= n-2
    while i>=0 and s[i]<=s[i + 1]:
        i-=1
    if i==-1:
        return -1
    j = n - 1
    while s[j] >= s[i]:
        j -= 1
    while (s[j]==s[j-1]):
        j-=1
    s[i], s[j] = s[j], s[i]
    if s[0] == '0':
        return -1
    return ''.join(s)
for _ in range(int(input())):
    s = input()
    print(solve(s))

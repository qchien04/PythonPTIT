def solve(s):
    i = 0
    while i < len(s):
        if s[i] == '6':
            if i + 2 < len(s) and s[i:i+3] == "688":
                i += 3
            elif i + 1 < len(s) and s[i:i+2] == "68":
                i += 2
            else:
                i += 1
        else:
            return "NO"
    return "YES"
s=input()
print(solve(s))
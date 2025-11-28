def solve(n):
    if n[0]==n[1]: return "NO"
    else:
        for i in range(2,len(n),2):
            if n[i]!=n[i-2]:
                return "NO"
        for i in range(3,len(n),2):
            if n[i]!=n[i-2]:
                return "NO"
    return "YES"
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=input()
        print(solve(n))

   
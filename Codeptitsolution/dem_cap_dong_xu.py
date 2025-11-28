def tohop(n):
    return n*(n - 1)//2

def cnt(n, a):
    ans = 0
    for i in a:
        count = i.count('C')
        ans += tohop(count)
    for j in range(n):
        count = sum(1 for i in range(n) if a[i][j] == 'C')
        ans += tohop(count)
    
    return ans

if __name__ == "__main__":
    n=int(input())
    a=[input() for _ in range(n)]
    result = cnt(n, a)
    print(result)

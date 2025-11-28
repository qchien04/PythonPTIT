def solve(b, n):
    a = [0]*n
    a[0] = (b[0][1] + b[0][2] - b[1][2]) // 2
    a[1] = b[0][1] - a[0]
    a[2] = b[0][2] - a[0]
    
    for i in range(3, n):
        a[i] = b[0][i] - a[0]
    
    return a
n = int(input())
if(n==2):
    a,b=map(int,input().split())
    a,b=map(int,input().split())
    print(a//2,a//2)
else: 
    b = []
    for i in range(n):
        b.append(list(map(int, input().split())))
    a = solve(b, n)
    print(" ".join(map(str,a)))






if __name__ == '__main__':
    t=int(input())
    e=[]
    while True:
        try: e.extend(map(int, input().split()))
        except: break
    c=0
    for _ in range(t):
        n,m=e[c],e[c+1]
        a=[]
        c+=2
        a = [[0 for _ in range(m)] for _ in range(n)]
        b = [[0 for _ in range(n)] for _ in range(m)]
        res=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                a[i][j]=e[c]
                c+=1
        for i in range(n):
            for j in range(m):
                b[j][i]=a[i][j]
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    res[i][j] += a[i][k] * b[k][j]
        for i in range(n):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
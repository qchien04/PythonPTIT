if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = [0] * 1001
        N = [0] * 1001
        dp1 = [1] * 1000
        res = -99999999
        for i in range(n):
            M[i],N[i]=map(float,input().split())
        for i in range(n):
            for j in range(i):
                if M[i] > M[j] and N[i] < N[j]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)
            res = max(res, dp1[i])
        print(res)

MOD = 10**9 + 7

def build_kmp(s):
    m = len(s)
    kmp = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and s[i] != s[j]:
            j = kmp[j-1]
        if s[i] == s[j]:
            j += 1
        kmp[i] = j
    return kmp

def count_strings_with_substring(N, M, s):
    m = len(s)
    
    if N < m:
        return 0

    kmp = build_kmp(s)
    
    # dp[i][j] sẽ là số lượng cách tạo ra xâu độ dài i với trạng thái j của KMP.
    dp = [[0] * m for _ in range(N + 1)]
    
    # Trạng thái ban đầu: xâu rỗng
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(m):
            for c in range(26):
                next_j = j
                char = chr(ord('a') + c)
                
                while next_j > 0 and s[next_j] != char:
                    next_j = kmp[next_j - 1]
                    
                if s[next_j] == char:
                    next_j += 1
                
                dp[i + 1][next_j] = (dp[i + 1][next_j] + dp[i][j]) % M
    
    # Tất cả các trạng thái mà đã hoàn thành xâu con s
    result = 0
    for j in range(m):
        result = (result + dp[N][j]) % M
    
    return result

# Input processing
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    s = input().strip()
    print(count_strings_with_substring(N, M, s))

def find_min_sum_b(n, a):
    b = [0] * n
    b[0] = 1  # Khởi tạo B[0] là 1
    
    for i in range(1, n):
        # Tính B[i] dựa vào công thức B[i] = A[i] * B[i-1] / A[i-1]
        b[i] = a[i] * b[i-1] // a[i-1]
    
    return sum(b)

# Đọc dữ liệu vào
n = int(input())
a = list(map(int, input().split()))

# Tính toán và in kết quả
result = find_min_sum_b(n, a)
print(result)
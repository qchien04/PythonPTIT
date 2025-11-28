def he10sanghe(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    
    return result

for _ in range(int(input())):
    n,base=map(int,input().split())
    print(he10sanghe(n,base))
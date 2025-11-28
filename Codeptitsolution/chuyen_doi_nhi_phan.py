def he10sanghe(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result
with open('DATA.in', 'r') as file:
    t = int(file.readline().strip()) 
    for _ in range(t):
        base=int(file.readline().strip())
        num=file.readline().strip()
        he10=int(num,2)
        print(he10sanghe(he10,base))
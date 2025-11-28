def he10to4(a):
    if a==0:
        return 0
    digits = '0123456789'
    res=''
    while a>0:
        res= digits[a % 4]+res
        a//=4
    return res

def chuyencoso(a,to):
    if a==0:return 0
    s='0123456789ABCDEFGHIJKLMNOP'
    res=''
    while a>0:
        res=s[a%to]+res
        a=a//to
    return res
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        coso=input()
        num=input()
        he10=int(num,2)
        print(chuyencoso(he10,int(coso)))
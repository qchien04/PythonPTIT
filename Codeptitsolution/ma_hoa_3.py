

# def rotate(s):
#     tong=0
#     for i in s:
#         tong+=(ord(i)-ord('A'))
#     result=""
#     for i in s:
#         c=chr((ord(i)-ord('A')+tong)%26+ord('A'))
#         result+=c
#     return result
# def merge(a,b):
#     result=""
#     for i in range(len(a)):
#         c=chr((ord(a[i])-2*ord('A')+ord(b[i]))%26+ord('A'))
#         result+=c
#     return result
# for _ in range(int(input())):
#     s=input()
#     mid=len(s)//2
#     a=rotate(s[:mid])
#     b=rotate(s[mid:])
#     print(merge(a,b))

def rotate(s):
    xoay=0
    for i in s:
        xoay+=ord(i)
    a=""
    for i in s:
        a+=chr((ord(i)-ord("A")+xoay)%26+ord("A"))
    return a
def merge(x,y):
    a=""
    k=0
    for i in x:
        a+=chr(((ord(i)-ord("A")+ord(y[k]))-ord("A"))%26+ord("A"))
        k+=1    
    return a
for _ in range(int(input())):
    s=input()
    l=len(s)//2
    print(merge(rotate(s[0:l]),rotate(s[l:])))
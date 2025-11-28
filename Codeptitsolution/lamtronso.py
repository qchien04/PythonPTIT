# import math

# if __name__ == '__main__':
#     t=int(input())
#     for _ in range(t):
#         s = input()
#         a=list(map(int,s[::-1]))
#         nho=0
#         for i in range(1,len(a)):
#             check=a[i-1]+nho
#             if(check>=5) :a[i]=a[i]+1
#             if(a[i]>5): nho=1
#             else: nho=0
#         print(a[len(a)-1],end="")
#         for _ in range(len(s)-1): print("0",end="")
#         print()

for _ in range(int(input())):
    s=input()
    a=list(map(int,s[::-1]))
    l=len(a)
    for i in range(1,len(s)):
        if a[i-1]>=5:a[i]+=1
    print(str(a[l-1])+"0"*(l-1))
    
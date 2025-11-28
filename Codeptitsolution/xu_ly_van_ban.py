import re
# import sys
# def chuanhoa(text):
#     arr=re.split(r'[.?!]', text)
#     res=[]
#     for i in arr:
#         print(i)
#         i=i.strip()
#         if not i:
#             continue
#         i=i.lower()
#         i=i.capitalize()   
#         i=re.sub(r'\s+', ' ', i)
#         res.append(i)
#     for i in res:
#         print(i)
# s=sys.stdin.read()
# chuanhoa(s)

s=""
while True:
    try:
        tmp=input().lower()
        s+=tmp
    except EOFError:
        break
s=re.sub(r"\s+"," ",s)
s=re.split(r"[.?!]",s)
for i in s:
    print(i.strip().capitalize())
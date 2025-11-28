import re

# for _ in range(int(input())):
#     s=input()
#     r="".join(re.findall(r"[)(]",s))
#     a=[0]*len(r)
#     b=[]
#     cnt=1
#     for i in range(len(r)):
#         if r[i]=="(":
#             a[i]=cnt
#             b.append(cnt)
#             cnt+=1
#         else:
#             a[i]=b[-1]
#             b.pop()
#     print(" ".join(str(x) for x in a))



for _ in range(int(input())):
    s=input()
    stt=1
    ans=[]
    rs=[]
    r="".join(re.findall(r"[)(]",s))
    for i in r:
        if i=="(":
            rs.append(stt)
            ans.append(stt)
            stt+=1
        else:
            ans.append(rs[-1])
            rs.pop()
    for i in ans:
        print(i,end=" ")
    print()
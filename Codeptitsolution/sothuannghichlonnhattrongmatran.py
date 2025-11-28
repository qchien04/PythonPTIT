
a=[]

# nt=[0]*10001

# nt[2]=1
# for i in range(math.sqrt(10001)):
#     if nt[i]==1:
#         for j in range(i*2,10001,i):
#             nt[j]=0
def tn(s):
    if s<10: return False
    s=str(s)

    if s==s[::-1]: return True
    return False
maxx=-1
n,m=map(int,input().split())
for _ in range(n):
    s=list(map(int,input().split()))
    a.append(s)
    for i in s:
        if(tn(i)):
            maxx=max(i,maxx)
if maxx==-1: print("NOT FOUND")
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if(a[i][j]==maxx):
                print(f"Vi tri [{i}][{j}]")


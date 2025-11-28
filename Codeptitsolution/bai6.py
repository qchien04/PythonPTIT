#ky tu abc

n=int(input())

def solve(i,string,len,a):
    if i==len:
        for j in range(3):
            if (a[j][1]==0): return
        if a[0][1]<=a[1][1]<=a[2][1]: print(string)
        return
    for c in "ABC":
        a[ord(c)-ord('A')][1]+=1
        solve(i+1,string+c,len,a)
        a[ord(c)-ord('A')][1]-=1

for i in range(3,n+1):
    a=[["A",0],["B",0],["C",0]]
    solve(0,"",i,a)


def solve(i,st,len,a):
    if i==len:
        for j in range(3):
            if a[j][1]==0: return
        if a[0][1]>a[1][1] or a[1][1]>a[2][1]: return 
        print(st)
        return
    for j in "ABC":
        a[ord(j)-ord('A')][1]+=1
        solve(i+1,st+j,len,a)
        a[ord(j)-ord('A')][1]-=1 

    
n=int(input())

for i in range(3,n+1):
    a=[["A",0],["B",0],["C",0]]
    solve(0,"",i,a)
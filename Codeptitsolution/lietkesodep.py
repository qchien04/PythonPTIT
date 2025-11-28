# arr = []
# def Try(i,n,s):
#     if s!= "" and s[0]=='0': return
#     if i==n: return arr.append(s+''.join(reversed(s)))
#     for j in range(0,9,2): Try(i+1,n,s+str(j))
# for i in range(1,5): Try(0,i,'')

# for t in range(int(input())):
#     n=int(input())
#     print(' '.join([x for x in arr if(int(x)<n)]))


a=['0','2','4','6','8']
ans=[]
def solve(s,n):
    if len(s)>3: return
    if len(s)>=1 and s[0]=='0': return
    if s!="":ans.append(int(s+s[::-1]))
    for i in a:
        solve(s+i,n)
solve("",4)
ans.sort()
for _ in range(int(input())):
    n=int(input())
    for i in ans:
        if i<n:
            print(i,end=" ")
    print()
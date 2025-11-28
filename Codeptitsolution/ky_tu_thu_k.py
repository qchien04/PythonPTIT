def solve(len,n,k):
    if n==1 or len==1: return "A"
    elif k==(len+1)/2:return chr(ord('A')+n-1)
    elif k<(len+1)/2: return solve((len-1)//2,n-1,k)
    else: return solve((len-1)//2,n-1,k-(len+1)//2)

for _ in range(int(input())):
    n,k=map(int,input().split())
    n1=n
    len=1
    while(n1>1):
        len=len*2+1
        n1-=1
    print(solve(len,n,k))
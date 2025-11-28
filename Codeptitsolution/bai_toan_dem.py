def kt(arr,n):
    minn=min(arr)
    maxx=max(arr)
    if maxx==n and len(arr)==n: 
        print("Excellent!")
        return
    for i in range(1,minn):
        print(i)
    for i in range(1,n):
        if arr[i]-arr[i-1]!=1:
            for j in range(arr[i-1]+1,arr[i]): print(j)
    for j in range(arr[n-1],maxx):
        print(j)
n=int(input())
arr=[]
while (len(arr)!=n):
    b=list(map(int,input().split()))
    arr+=b
kt(arr,n)


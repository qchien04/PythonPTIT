n=int(input())

A=list(map(int,input().split()))
A.sort()
ans=max(A[-1] * A[-2], A[-1] * A[-2] * A[-3],A[0] * A[1] * A[-1],A[0] * A[1])

print(ans)
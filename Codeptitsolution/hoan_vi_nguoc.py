# import itertools

# t=int(input())
# for _ in range(t):

#     n=int(input())
#     arr=range(1,n+1)
#     hv = list(itertools.permutations(arr))
#     print(len(hv))
#     for i in range(len(hv)-1,-1,-1):
#         print(*hv[i],sep="",end=" ")
#     print()

import itertools

for _ in range(int(input())):
    arr=range(1,int(input())+1)
    arr=list(itertools.permutations(arr))
    print(len(arr))
    for i in range(len(arr)-1,-1,-1):
        print(*arr[i],sep="",end=" ")
    print()
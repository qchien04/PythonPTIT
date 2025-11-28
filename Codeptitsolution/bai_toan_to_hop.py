# n=0
# k=0
# arr=[]
# def cre(i,dayso,cnt):
#     if cnt==k:
#         print(dayso)
#     for j in range(i,n):
#         cre(j+1,dayso+str(arr[j])+" ",cnt+1)
import itertools
if __name__ == '__main__':
    n,k=map(int,input().split())
    arr=list(set(map(int,input().split())))
    n=len(arr)
    arr.sort()
    ans=list(itertools.combinations(arr,k))
    for i in ans:
        print(*i)
    # cre(0,"",0)

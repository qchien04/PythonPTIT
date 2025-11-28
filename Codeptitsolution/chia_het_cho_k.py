import math
if __name__ == '__main__':
    a,k,n=map(int,input().split())

    start=math.ceil(a/k)
    end=math.floor(n/k)
    check=False
    for i in range(start,end+1):
        if i*k-a!=0:
            print(i*k-a,end=" ")
            check=True
    if not check: print("-1")

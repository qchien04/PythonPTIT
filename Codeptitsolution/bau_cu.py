from collections import Counter

def kt(arr,n):
    se=set()
    a=[[i,0] for i in range(1,n+1)]
    for i in arr:
        a[i-1][1]=a[i-1][1]+1
    a=sorted(a,key=lambda x:(-x[1],x[0]))
    for i in a:
        if(i[1]!=0):
            se.add(i[1])
    if len(se)==1: return "NONE"
    else:
        b=sorted(se)
    chuan=b[-2]
    for i in a:
        if(i[1]==chuan):
            return i[0]
    return "NONE"

    print(a)
if __name__ == '__main__':
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(kt(arr,k))
    
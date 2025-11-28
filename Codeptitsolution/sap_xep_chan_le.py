import math

if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    while len(a)<n:
        a.extend(list(map(int,input().split())))
    le=sorted([x for x in a if x%2==1],key=lambda x:-x)
    chan=sorted([x for x in a if x%2==0])
    k=0
    j=0
    for i in a:
        if i%2==0:
            print(chan[j],end=" ")
            j+=1
        else:
            print(le[k],end=" ")
            k+=1
    
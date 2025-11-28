from collections import Counter
import math
nt=[1]*1000001
nt[0]=nt[1]=0
arr=[]
def sang():
    for i in range (2,int(math.sqrt(1000001))):
        if nt[i]==1:
            arr.append(i)
            for j in range (i*i,1000001,i):
                nt[j]=0
def kt(i):
    if nt[int(i)]==1: return i
    return None
if __name__ == '__main__':
    sang()
    n=int(input())
    arr = list(filter(None, map(kt, input().split())))
    lis=dict(Counter(arr))
    for i in lis.items():
        print(i[0],i[1])
import math
vs=[1]*100
a=[0]*100
n=""
def hv(i):
    if i>=len(n):
        for i in range(0,len(n)):
            print(n[a[i]],end="")
        print()
        return
    for j in range(0,len(n)):
        if vs[j]==1:
            a[i]=j
            vs[j]=0
            hv(i+1)
            vs[j]=1       
        
if __name__ == '__main__':
    n=input()
    hv(0)
import math
def nt(x):
    if x<2: return False
    if x==2: return True
    if x%2==0: return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x%i==0: return False
    return True
def dk2(n):
    s1=str(n)
    sum=0
    for i in s1:
        sum+=int(i)
        if(nt(int(i))==0): return False
    if(nt(sum)==0): return False
    s2=s1[::-1]
    if(nt(int(s2))==0): return False
    return True

    

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        num=int(input())
        print("Yes") if dk2(num) else print("No")
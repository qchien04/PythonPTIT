
def tich(n):
    t=1
    for i in n:
        t*=int(i)
    return t
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(input().split())
        b=sorted(a,key=lambda x:(tich(x),int(x)))
        for i in b:
            print(i,end=" ")
        print()
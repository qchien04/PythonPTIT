
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        arr=list(map(int,input().split()))
        for i in arr[b:]:
            print(i,end=" ")
        for i in arr[:b]:
            print(i,end=" ")
        print()
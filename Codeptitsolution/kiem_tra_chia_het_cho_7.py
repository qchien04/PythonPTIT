
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=input()
        check=False
        for _ in range(0,1000):
            if(int(n))%7==0:
                print(int(n))
                check=True
                break;
            n=str(int(n)+int(n[::-1]))
            #print(n)
        if not check: print("-1")
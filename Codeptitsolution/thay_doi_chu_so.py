
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        maxx,minn=input().split()
        s=input().split()
        if(len(s)>1):
            num1,num2=s[0],s[1]
        else:
            num1=s[0];
            num2=input()
        
        if(int(maxx)<int(minn)): maxx,minn=minn,maxx
        n1=int(num1.replace(maxx,minn))
        n2=int(num2.replace(maxx,minn))
        n3=int(num1.replace(minn,maxx))
        n4=int(num2.replace(minn,maxx))
        print(n1+n2,n3+n4)

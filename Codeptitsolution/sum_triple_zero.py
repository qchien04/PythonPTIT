if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=input()
        a=list(map(int,input().split()))
        a.sort()
        ans=0
        for i in range(0,len(a)-2):
            if(a[i]>0): break
            l=i+1
            r=len(a)-1
            while(l<r):
                sum=a[i]+a[r]+a[l]
                if(sum==0):
                    ans+=1
                    l+=1
                if(sum<0):
                    l+=1
                if(sum>0):
                    r-=1
        print(ans)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=input()
        a=list(map(int,input().split()))
        a.sort()
        ans=0
        for i in range(0,len(a)-2):
            cur=a[i]
            if(cur>0): break
            l=i+1
            r=len(a)-1
            while(l<r):
                if(cur+a[r]+a[l]==0):
                    ans+=1
                    l+=1
                if(cur+a[r]+a[l]<0):
                    l+=1
                if(cur+a[r]+a[l]>0):
                    r-=1
        print(ans)
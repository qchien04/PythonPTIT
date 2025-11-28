

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        st=[]
        cnt=1
        b=[0]*100001
        for i in range(0,n):
            while st and a[i]>=a[st[-1]]:
                st.pop()
            if st:
               b[i]=i-st[-1]
            else: b[i]=i+1
            st.append(i)
        for i in range(n):
            print(b[i],end=" ")
        print()

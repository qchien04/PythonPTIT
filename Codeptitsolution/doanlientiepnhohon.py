

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    st=[]
    res=[0]*len(arr)
    st.append(-1)
    for i in range(0,len(arr)):
        while len(st)>1 and arr[st[-1]]<=arr[i]:
            st.pop() 

        res[i]=i-st[-1]
        st.append(i)
    for i in res:
        print(i,end=" ")
    print()


            
if __name__ == '__main__':
    n = int(input())
    arr=[]
    for _ in range(n):
        st=str(input())
        func,*detail=st.split()
        if func=='append':
            for i in detail:
                arr.append(int(i))
        elif func=='print':
            print(arr)
        elif func=='remove':
            arr.remove(int(detail[0]))
        elif func=='insert':
            pos,num=detail
            arr.insert(int(pos),int(num))
        elif func=='sort':
            arr.sort()
        elif func=='pop':
            arr.pop()
        elif func=='reverse':
            arr.reverse()
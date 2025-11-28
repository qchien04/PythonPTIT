a=[]
def creNum(i,l,num,n):
    global a
    if i<=l :
        s=num
        if i!=0:
            s+=s[::-1]
            if int(s) < n:
                a.append(int(s))
        for j in range(0,9,2):
            if(num=="") and j==0:
                continue
            creNum(i+1,l,num+str(j),n)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        a=[]
        s=input()
        l=int(len(s)/2)
        creNum(0,l,"",int(s))
        a.sort()
        for i in a:
            print(i,end=" ")
        print()
            
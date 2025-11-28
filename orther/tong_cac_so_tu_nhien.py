a=[]
n=0
def sinh(sum,s,head):
    global a,n 
    for i in range(head,0,-1):
        if sum==n:
            a.append(f"({s.strip()})")
            return
        elif sum<n:
            sinh(sum+i,s+str(i)+" ",i)

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        sinh(0,"",n)
        print(len(a))
        for i in a:
            print(i,end=" ")
        a.clear()
        print()

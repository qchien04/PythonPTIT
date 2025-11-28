import bisect

if __name__=="__main__":
    nonPrime=[]
    cnt=[0]*(10**5+1)
    maxx=0
    for i in range(2,10**5):
        for j in range(i,10**5,i):
            cnt[j]+=1
        
        if cnt[i]>maxx:
            maxx=cnt[i]
            nonPrime.append(i)
    for _ in range(int(input())):
        n=int(input())
        print(n)
        index=bisect.bisect_right(nonPrime,n)
        print(nonPrime[index])
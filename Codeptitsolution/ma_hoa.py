
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        s=input()
        num=1
        w=s[0]
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                print(str(num)+w,end="")
                w=s[i]
                num=1  
            else: num+=1
        print(str(num)+w)
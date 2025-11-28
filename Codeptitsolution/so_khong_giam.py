
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        s=input()
        check=False
        for i in range (1,len(s)):
            if s[i]<s[i-1]: 
                check=True
                break
        print("NO") if check else print("YES")
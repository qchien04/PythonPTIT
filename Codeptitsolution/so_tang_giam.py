def check(n):
    if len(n)<3: 
        return False
    i=0
    while i<len(n)-1 and n[i]<n[i+1]: 
        i+=1
    while i<len(n)-1 and n[i]>n[i+1]: 
        i+=1
    return i==len(n)-1
if __name__ == '__main__':
    for t in range(int(input())):
        n=input()
        print("YES") if check(n) else print("NO")
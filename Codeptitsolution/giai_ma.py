import re
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        s=input()
        letters = re.findall(r'[a-zA-Z]+', s)
        numbers = list(map(int,re.findall(r'\d+', s)))
        for i in range(len(letters)):
            s1=letters[i]*numbers[i]
            print(s1,end="")
        print()

        

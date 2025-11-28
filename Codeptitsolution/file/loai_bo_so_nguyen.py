import re

if __name__=="__main__":
    pattern=r"^\d{1,8}$"
    with open("DATA.in","r") as file:
        a = []
        maxx = 0
        for line in file:
            s = line.strip().split()
            for i in s:
                if re.match(pattern,i):continue
                else:
                    a.append(i)
        a.sort()
        for i in a:
            print(i,end=" ")
    
                
            


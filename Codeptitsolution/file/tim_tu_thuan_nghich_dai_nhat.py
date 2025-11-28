from collections import defaultdict
def tn(s):
    r=s[::-1]
    return s==r
if __name__=="__main__":

    with open("VANBAN.in","r") as file:
        d = defaultdict(int)
        a = []
        maxx = 0
        for line in file:
            s = line.strip().split()
            for i in s:
                if tn(i):
                    d[i] += 1
                    if d[i] == 1:
                        a.append(i)
                    maxx = max(maxx, len(i))
        for i in a:
            if len(i) == maxx:
                print(i, d[i])
    
                
            


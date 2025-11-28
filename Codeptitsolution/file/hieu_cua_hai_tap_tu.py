
if __name__=="__main__":
    se1=set()
    se2=set()
    with open("DATA1.in","r") as file:
        for line in file:
            s = line.lower().strip().split()
            se1.update(s)
    with open("DATA2.in","r") as file2:
        for line in file2:
            s = line.lower().strip().split()
            se2.update(s)
    a = sorted(se1 - se2)
    b = sorted(se2 - se1)
    print(" ".join(a))
    print(" ".join(b))

    
                
            


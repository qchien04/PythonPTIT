class GV:

    def __init__(self,n,name,code,p1,p2) -> None:
        if(n<10):
            self.ma="GV0"+str(n)
        else:self.ma="GV"+str(n)
        self.name=name
        self.code=code
        self.p1=p1
        self.p2=p2
        self.xl=None
    def getDiemUutien(self):
        pr=self.code[1]
        if pr=="1":
            return 2.0
        elif pr=="2": return 1.5
        elif pr=="3": return 1.0
        return 0.0
    def getTotal(self):
        return self.p1*2+self.p2+self.getDiemUutien()
    def getSub(self):
        sub=self.code[0]
        if sub=="A":
            return "TOAN"
        elif sub=="B": return "LY"
        return "HOA"
    def getTt(self):
        total=self.getTotal()
        if total>=18.0: self.xl= "TRUNG TUYEN"
        else: self.xl="LOAI"
    def __str__(self) -> str:
        self.getTt()
        return self.ma+" "+self.name+" "+self.getSub()+" "+str(self.getTotal())+" "+self.xl


if __name__=="__main__":
    a=[]
    n=0
    for _ in range(int(input())):
        name=input()
        code=input()
        p1=float(input())
        p2=float(input())
        n+=1
        newgv=GV(n,name,code,p1,p2)
        a.append(newgv)
    a=sorted(a,key=lambda x:-x.getTotal())
    for i in a:
        print(i)

    
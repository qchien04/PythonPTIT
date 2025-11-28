class NhanVien:
    stt=0
    def __init__(self,name,d1,d2) -> None:
        self.name=name
        NhanVien.stt+=1
        self.code="TS0"+str(NhanVien.stt)
        self.d1=d1
        self.d2=d2
    def getTb(self):
        return (self.d1+self.d2)/2
    def getXl(self):
        d=self.getTb()
        if d>9.5:return "XUAT SAC"
        if d>=8:return "DAT"
        if d>=5:return "CAN NHAC"
        return "TRUOT"
    def __str__(self) -> str:
        return self.code+" " +self.name+" "+f"{self.getTb():.2f} "+self.getXl()


if __name__ == '__main__':
    n=int(input())
    a=[]
    for i in range(n):
        name=input()
        d1=float(input())
        if d1>10:
            d1=int(d1)
            s=str(d1)[0]+"."+str(d1)[1:]
            d1=float(s)
        d2=float(input())
        if d2>10:
            d2=int(d2)
            s=str(d2)[0]+"."+str(d2)[1:]
            d2=float(s)
        a.append(NhanVien(name,d1,d2))
    a=sorted(a,key=lambda x:-x.getTb())
    for i in a:
        print(i)
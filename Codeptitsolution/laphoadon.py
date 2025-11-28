
from datetime import datetime
class Hoadon:
    stt=0
    def __init__(self,name,phong,n1,n2,tien):
        Hoadon.stt+=1
        self.id=f"KH{Hoadon.stt:02d}"
        self.name=name
        self.phong=phong
        self.n1=n1
        self.n2=n2
        self.tien=tien

    def getgia(self):
        tang=int(self.phong[0])
        if tang==1: return 25
        if tang==2: return 34
        if tang==3: return 50
        return 80
    def getngay(self):
        d1=datetime.strptime(self.n1,"%d/%m/%Y")
        d2=datetime.strptime(self.n2,"%d/%m/%Y")
        return (d2-d1).days+1
    def gettien(self):
        return self.getngay()*self.getgia()+self.tien
    def __str__(self):
        return f"{self.id} {self.name} {self.phong} {self.getngay()} {self.gettien()}"

a=[]
for _ in range(int(input())):
    name=input().strip()
    phong=input().strip()
    n1=input().strip()
    n2=input().strip()
    tien=int(input())
    hoadon=Hoadon(name,phong,n1,n2,tien)
    a.append(hoadon)
a=sorted(a,key=lambda i:-i.gettien())
for i in a:
    print(i)
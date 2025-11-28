class thisinh:
    def __init__(self,name,donvi,td) -> None:
        self.ma="".join(map(f,donvi.split()))+"".join(map(f,name.split()))
        self.name=name
        self.donvi=donvi
        self.td=td
        self.v=self.vt()
    def vt(self):
        h,m=self.td.split(":")
        h=int(h)-6
        m=int(m)/60
        t=h+m
        return 120/t
    
    def __str__(self) -> str:
        return self.ma+" "+self.name+" "+self.donvi+" "+f"{self.v:.0f}"+" Km/h"


3464485328

def f(s):
    return s[:1].upper()
if __name__ == '__main__':
    a=[]
    for _ in range(int(input())):
        name=input()
        donvi=input()
        td=input()
        ts=thisinh(name,donvi,td)
        a.append(ts)
    a=sorted(a,key=lambda x:-x.v)
    for i in a : print(i)
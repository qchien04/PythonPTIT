class Student:
    def __init__(self,ma,name,lop) -> None:
        self.name=name
        self.ma=ma
        self.lop=lop
        self.diem=0
    def __str__(self) -> str:
        return self.ma+" "+self.name+" "+self.lop+" "+str(self.diem)+" "+f"{'KDDK' if self.diem==0 else ''}"
    def tinhdiem(self,v,m):
        self.diem=10-2*v-m
        if self.diem<0: self.diem=0

if __name__ == '__main__':
    a=[]
    t=int(input())
    for _ in range(t):
        ma=input()
        name=input()
        lop=input()
        st=Student(ma,name,lop)
        a.append(st)
    for _ in range(t):
        ma,s=input().split()
        s=list(s)
        v=s.count("v")
        m=s.count("m")
        for i in a:
            if i.ma==ma:
                i.tinhdiem(v,m)
    for i in a:
        print(i)
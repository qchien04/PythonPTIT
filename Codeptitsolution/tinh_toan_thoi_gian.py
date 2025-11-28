from datetime import datetime
fmt="%H:%M"
class Gamer:
    def __init__(self,code,name,inp,outp) -> None:
        self.name=name
        self.code=code
        self.inp=datetime.strptime(inp,fmt)
        self.outp=datetime.strptime(outp,fmt)
    def getPlayTime(self):
        s=(self.outp - self.inp).total_seconds()
        h = int(s // 3600) 
        m = int((s % 3600) // 60)
        return [h,m]
    def __str__(self) -> str:
        h,m=self.getPlayTime()
        return self.code+" "+self.name+" "+f"{h} gio {m} phut"


if __name__=="__main__":
    n=int(input())
    a=[]
    for _ in range(n):
        code=input()
        name=input()
        inp=input()
        outp=input()
        a.append(Gamer(code,name,inp,outp))
    a=sorted(a,key=lambda x:(-x.getPlayTime()[0],-x.getPlayTime()[1]))
    for i in a:
        print(i)
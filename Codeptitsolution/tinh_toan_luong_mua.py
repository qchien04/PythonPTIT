from datetime import datetime
fmt="%H:%M"
class OB:
    stt=1
    def __init__(self,name,t1,t2,quantity) -> None:
        self.name=name
        self.code=f"T{OB.stt:02d}"
        OB.stt+=1
        self.quantity=quantity
        self.t=OB.getRainTime(t1,t2)
    def getRainTime(t1,t2):
        t1=datetime.strptime(t1,fmt)
        t2=datetime.strptime(t2,fmt)
        return (t2 - t1).seconds/3600

    def getTb(self):
        return self.quantity/self.t
    def __str__(self) -> str:
        return self.code+" "+self.name+" "+f"{self.getTb():.2f}"

if __name__=="__main__":
    dic=dict()
    for _ in range(int(input())):
        name=input()
        t1=input()
        t2=input()
        quantity=int(input())
        if name in dic.keys():
            dic[name].quantity+=quantity
            dic[name].t+=OB.getRainTime(t1,t2)
        else:
            ob=OB(name,t1,t2,quantity)
            dic[name]=ob

    for i in dic.keys():
        print(dic[i])
    
        

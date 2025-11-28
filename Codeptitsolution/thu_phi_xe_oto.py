
class Bill:
    def __init__(self,id,type,place,io,time) -> None:
        self.id=id
        self.type=type
        self.place=int(place)
        self.io=io
        self.time=time
    def getBill(self):
        if self.type=="Xe_con":
            if self.place==5:return 10000
            else: return 15000
        elif self.type=="Xe_tai": return 20000
        elif self.type=="Xe_khach":
            if self.place==29:return 50000
            else: return 70000

if __name__=="__main__":
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
        id,type,place,io,time=input().split()
        if io=="IN":
            b.append(Bill(id,type,place,io,time))
        if time not in a:
            a.append(time)
    for i in a:
        print(i+": ",end="")
        sum=0
        for j in b:
            if j.time==i:
                sum+=j.getBill()
        print(sum)


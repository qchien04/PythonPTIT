class HD:
    def __init__(self,id,name,quantity,cost,ck) -> None:
        self.id=id
        self.name=name
        self.quantity=quantity
        self.cost=cost
        self.ck=ck
    def getTotal(self):
        return self.cost*self.quantity-self.ck
    def __str__(self) -> str:
        return self.id+" "+ self.name+" "+str(self.quantity)+" "+\
                str(self.cost)+" "+str(self.ck)+" "+str(self.getTotal())
    

arr=[]
for _ in range(int(input())):
    id=input()
    name=input()
    quantity=int(input())
    cost=int(input())
    ck=int(input())
    arr.append(HD(id,name,quantity,cost,ck))

res=sorted(arr,key= lambda x:-x.getTotal())

for i in res:
    print(i)
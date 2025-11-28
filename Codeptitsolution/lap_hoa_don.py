class Customer:
    stt=0
    def __init__(self,name,s) -> None:
        Customer.stt+=1
        self.name=name
        self.ma=f"KH{Customer.stt:02d}"
        self.tien=0
        if s<=50:
            self.tien=s*102
        elif s<=100:
            self.tien=(50*100+(s-50)*150)/100*103
        else :
            self.tien=(50*100+50*150+(s-100)*200)/100*105
    def __str__(self) -> str:
        return self.ma+" "+self.name+" "+f"{self.tien:.0f}"


if __name__ == '__main__':
    arr=[]
    for _ in range(int(input())):
        name=input()
        a=int(input())
        b=int(input())
        s=b-a
        k=Customer(name,s)
        arr.append(k)
    arr=sorted(arr,key=lambda x:(-x.tien,x.ma))
    for i in arr:
        print(i)
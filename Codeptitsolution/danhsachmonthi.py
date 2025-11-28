

class Mon:
    def __init__(self,ma,ten,ht) -> None:
        self.ma=ma
        self.ten=ten
        self.ht=ht
    def __str__(self) -> str:
        return f"{self.ma} {self.ten} {self.ht}"

arr=[]
for _ in range(int(input())):
    ma=input()
    ten=input()
    ht=input()
    arr.append(Mon(ma,ten,ht))

arr=sorted(arr,key=lambda x:x.ma)

for i in arr:
    print(i)
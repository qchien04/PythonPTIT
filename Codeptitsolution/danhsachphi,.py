

class Phim:
    stt=0
    def __init__(self,ma,ngay,ten,sotap) -> None:
        Phim.stt+=1
        self.code=f"P{Phim.stt:03d}"
        self.ma=ma
        self.ten=ten
        self.date=ngay
        self.ngay=list(map(int,ngay.split("/")))
        self.sotap=sotap
    def __str__(self) -> str:
        return f"{self.code} {self.ma} {self.date} {self.ten} {self.sotap}"

arr=[]
tl=[]
m,n=map(int,input().split())
for i in range(m):
    tl.append(input())
for _ in range(n):
    ma=tl[int(input()[2:])-1]
    ngay=input()
    ten=input()
    sotap=int(input())
    arr.append(Phim(ma,ngay,ten,sotap))
arr=sorted(arr,key=lambda x:(x.ngay[2],x.ngay[1],x.ngay[0],x.ten,-x.sotap))

for i in arr:
    print(i)

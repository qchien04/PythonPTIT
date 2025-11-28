import math
class PhanSo:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def __str__(self) -> str:
        g=math.gcd(self.a,self.b)
        return f"{self.a/g:.0f}/{self.b/g:.0f}"
    def __add__(self,other):
        aNew=self.a*other.b+other.a*self.b
        bNew=self.b*other.b
        return PhanSo(aNew,bNew)


if __name__ == '__main__':
    a,b,c,d=map(int,input().split())
    ps1=PhanSo(a,b)
    ps2=PhanSo(c,d)
    res=ps1+ps2
    print(res)
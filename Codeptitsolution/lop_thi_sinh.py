class Student:
    def __init__(self,name,birth,d1,d2,d3) -> None:
        self.name=name
        self.birth=birth
        self.d1=d1
        self.d2=d2
        self.d3=d3
    def __str__(self) -> str:
        return name+" "+birth+" "+f"{(self.d1+self.d2+self.d3):.1f}"

if __name__ == '__main__':
    name=input()
    birth=input()
    d1,d2,d3=float(input()),float(input()),float(input())
    st=Student(name,birth,d1,d2,d3)
    print(st)
import math

class Point:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def d(self, other):
        a = self._x - other.get_x()
        b = self._y - other.get_y()
        dis = math.sqrt(a * a + b * b)
        return dis

class Triangle:
    def __init__(self, p1, p2, p3) -> None:
        self.a = p1.d(p2)
        self.b = p2.d(p3)
        self.c = p3.d(p1)
    
    def chuvi(self):
        if (self.a + self.b <= self.c or
            self.a + self.c <= self.b or
            self.b + self.c <= self.a):
            return "INVALID"
        else:
            return f"{self.a + self.b + self.c:.3f}"
    def dientich(self):
        if (self.a + self.b <= self.c or
            self.a + self.c <= self.b or
            self.b + self.c <= self.a):
            return "INVALID"
        else:
            x=(self.a + self.b + self.c)*(self.a + self.b - self.c)*(self.a - self.b + self.c)*(-self.a + self.b + self.c)
            y=math.sqrt(x)/4
            return f"{y:.2f}"
    
if __name__ == '__main__':
    t = int(input())
    l = []
    for i in range(t): l.extend([float(x) for x in input().split()])
    i=0
    #print(len(l))
    for j in range(t):
        a, b, c, d, e, f =l[i],l[i+1],l[i+2],l[i+3],l[i+4],l[i+5]
      #  print(a,b,c,d,e,f)
        p1 = Point(a, b)
        p2 = Point(c, d)
        p3 = Point(e, f)
        tg = Triangle(p1, p2, p3)
        print(tg.dientich())
        i+=6

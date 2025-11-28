import sys
a = sys.stdin.read()
a = a.split()
a.insert(2, '1')

def input():
    return " ".join(a[:3])

class Rectangle:
    def __init__(self, x, y, z) -> None:
        self.z = 1
        if x <= 0 or y <= 0:
            print("INVALID")
            self.z = 0
        self.x = x
        self.y = y

    def area(self):
        if self.z:
            return self.x * self.y
        return ""

    def perimeter(self):
        if self.z:
            return self.x * 2 + self.y * 2
        return ""

    def color(self):
        if self.z:
            return a[-1].title()  
        return ""

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))

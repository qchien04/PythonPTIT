from decimal import Decimal, ROUND_HALF_UP

class Student:
    stt = 0

    def __init__(self, name, d1, d2, d3):
        self.name = ' '.join([word.capitalize() for word in name.strip().split()])
        Student.stt += 1
        self.ma = f"SV{Student.stt:02d}"
        self.d1 = Decimal(str(d1))
        self.d2 = Decimal(str(d2))
        self.d3 = Decimal(str(d3))
        self.total = (self.d1 * 3 + self.d2 * 3 + self.d3 * 2) / 8
        self.total = self.total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def get_total(self):
        return self.total

    def __str__(self):
        return f"{self.ma} {self.name} {self.total:.2f}"

if __name__ == "__main__":
    t = int(input())
    students = []
    for _ in range(t):
        name = input().strip()
        d1 = Decimal(input().strip())
        d2 = Decimal(input().strip())
        d3 = Decimal(input().strip())
        students.append(Student(name, d1, d2, d3))

    students.sort(key=lambda x: x.get_total(), reverse=True)

    print(f"{students[0]} 1")
    stt = 1
    for i in range(1, len(students)):
        current = students[i]
        previous = students[i - 1]
        print(current, end=" ")
        if current.get_total() == previous.get_total():
            print(stt)
        else:
            stt = i + 1
            print(stt)

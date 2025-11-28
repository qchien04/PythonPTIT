class Car:
    # Thuộc tính lớp (class variable)
    wheels = 4
    
    def __init__(self, make, model, year):
        # Thuộc tính đối tượng (instance variables)
        self.make = make
        self.model = model
        self.year = year
    
    def get_description(self):
        # Phương thức đối tượng
        return f"{self.year} {self.make} {self.model}"
    def get_id(self):
        # Phương thức đối tượng
        return self.id
    
    @classmethod
    def number_of_wheels(cls):
        # Phương thức lớp
        return cls.wheels
    
    @staticmethod
    def is_motor_vehicle():
        # Phương thức tĩnh
        return True

# Tạo đối tượng của lớp Car
my_car = Car("Toyota", "Corolla", 2023)

# Gọi phương thức đối tượng
print(my_car.get_description())  # Output: 2023 Toyota Corolla

# Gọi phương thức lớp
print(Car.number_of_wheels())  # Output: 4

# Gọi phương thức tĩnh
print(Car.is_motor_vehicle())  # Output: True

my_car.id="10001"
print(my_car.get_description())

print(my_car.get_id())

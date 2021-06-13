class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + '@gmail.com'
    def fullname(self):
        print(self.first + ' ' + self.last)

Josefina = Employee('Josefina', 'Costa', 90000)
Josefina.fullname()

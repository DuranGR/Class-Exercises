class Employee:
    raise_ammount = 1.05
    num_workers = 0
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + '@gmail.com'
        Employee.num_workers += 1
    def fullname(self):
        print(self.first + ' ' + self.last)
    def apply_raise(self):
        self.salary = self.salary * self.raise_ammount
    
    @classmethod
    def set_raise_ammount(cls, ammount):
        cls.raise_ammount = ammount
    
    @classmethod
    def employee_str(cls, string):
        first, last, salary = string.split('-')
        return cls(first, last, salary)
    @staticmethod
    def is_workday(weekday_num):
        if weekday_num == 7 or weekday_num == 1:
            return False
        else:
            return True
        
josefina = Employee('Josefina', 'Costa', 100)
james = Employee('James', 'Souza', 200)

josefina.apply_raise()
Employee.set_raise_ammount(1.10)
james.apply_raise()
print(josefina.salary, james.salary)

emp_1 = "Jorge-Santos-1000"
jorge = Employee.employee_str(emp_1)

jorge.salary = int(jorge.salary)
jorge.apply_raise()
print(jorge.salary)

print(Employee.is_workday(2))

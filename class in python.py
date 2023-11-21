class Employee:
    raise_amount=1.04
    def __init__(self,name,lname,age,pay):
        self.fname=name
        self.lname=lname
        self.age=age
        self.pay=pay
        self.email=name +lname+ str(age) +"@gmail.com"
    def fullname(self):
        return f"my full name is {self.fname} {self.lname}"
    def apply_raise(self):
        return self.pay = self.pay * Employee.raise_amount
emp_1=Employee('Anurag','kumar',20,4000000)
emp_2=Employee('Sahil','khan',20,89000)
# print(emp_2.email)
# print(emp_1)
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))
print(emp_1.raise_amount)
print(emp_1.pay)
print(emp_1.apply_raise())
print(Employee.apply_raise(emp_2))
emp_1.raise_amount=1.07
print(emp_2.raise_amount)
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_1.__dict__)
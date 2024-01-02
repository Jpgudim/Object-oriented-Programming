"""
This is a basic practice program to learn object-oriented programming
Using the guide written on realpython.com
"""

# creating a class known as employee, which creates an employee object with name, job, and salary instance attributes and a company class attribute
class employee:
    company = "Microsoft"
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

# instantiating a class
john = employee("John", "accountant", 80000)

print(john.name)
print(john.job)
print(john.salary)
print(john.company)

john.salary += 10000
print(john.salary)


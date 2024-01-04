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
    # adding an instance method
    def description(self):
        print("%s is a %s that makes %i dollars a year" % (self.name, self.job, self.salary))
    # testing if an instance method can change an instance attribute
    def yearlyraise(self):
        self.salary += 3000

# instantiating a class
john = employee("John", "accountant", 80000)

print(john.name)
print(john.job)
print(john.salary)
print(john.company)

# updating an instance attribute
john.salary += 10000
print(john.salary)

# calling an instance method
john.description()

john.yearlyraise()
john.description()


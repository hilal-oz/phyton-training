import numbers
class Employee:
   # def __int__(self):  #default no argument constructor
     #   self.name=None
      #  self.job_title=None
       # self.salary=None
   is_human=True
   def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
       self.name = name
       self.job_title = job_title
       self.salary = salary


   def work(self):
        print(f'{self.name} is working')
 #  def __str__(self):
  #     return f'name: {self.name},job_title:{self.job_title}'

   def __str__(self):
       return f'{type(self).__name__}{self.__dict__}'

employee1 = Employee()

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Daniel')

print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

employee3 = Employee('Breanna', 'SDET')

print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

employee4 = Employee('Yulia', 'Python Developer', 150_000)
print(employee4.name)
print(employee4.job_title)
print(employee4.salary)

print(Employee.is_human) #true

employee1.work()
employee3.work()

print(employee2)   #name: Daniel,job_title:Janitor


print(employee1)
print(employee2)
print(employee3)
print(employee4) #Employee{'name': 'Yulia', 'job_title': 'Python Developer', 'salary': 150000}

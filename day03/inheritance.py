class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):

    def __init__(self, name: str, age: int, job_title: str, company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age)  # calling parent class' constructor
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')


class Developer(Employee):
    pass # you should give pass in python block cannot be empty
    #calling implicitly i f we dont need extra variables, if we need addtional variable manually call that time

    def work(self):
        print(f'{self.job_title} {self.name} is coding')

class Teacher(Employee):

    def __init__(self, name: str, age: int, job_title: str = "Teacher", company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age, job_title, company_name, salary) # calling parent class' constructor

    def work(self):
        print(f'{self.name} is teaching')




employee1=Employee("Hazel",27,'QA','Apple',120000)
developer1=Developer('Daniel',35, 'Java Dev','SpaceX')

person1=Person('Julia',32)
teacher = Teacher('Breanna', 45 )

print(employee1)
print(developer1)
print(teacher) #Teacher{'name': 'Breanna', 'age': 45, 'job_title': 'Teacher', 'company_name': 'Unknown', 'salary': 0}

employee1.work()
developer1.work()
teacher.work()#Breanna is teaching

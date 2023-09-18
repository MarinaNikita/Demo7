git class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.surname = lastname

    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}'

person1 = Person('Vasya', 'Petrov')
person2 = Person('Masha', 'Ivanova' )
print(person1.hello())
print(person2.hello())

class Teacher(Person):
    def __init__(self, name, lastname, field):
        super().__init__(name, lastname)
        self.field = field

    def greet(self):
        return f'{self.hello()} , I work in {self.field}'

teacher1 = Teacher('Snezhanna', 'Denisovna', 'literature')
teacher2 = Teacher('Igor', 'Petrovich', 'biology')
print(teacher1.greet())
print(teacher2.greet())

class Student(Person):
    def __init__(self, name, lastname, grade, age):
        super().__init__(name, lastname)
        self.__grade = grade
        self.__age = age

    def answer(self):
        return f'{self.hello()} , i have {self.__grade}'

    def set_grade(self, new_grade):
        self.__grade = new_grade

    def get_grade(self):
        return self.__grade


    def set_age(self, new_age):
        self.__age = new_age

    def get_age(self):
        return self.__age

student1 = Student('Harry', 'Potter', 5, 20)
print(student1._Student__grade)
print(student1.get_grade())
student1.set_grade(3)
print(student1.get_grade())
student1.set_age(35)
print(student1.get_age())
print(student1.__dict__)
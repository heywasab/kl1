class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_info(self):
          print(f"Name: {self.name}, Age: {self.age}")  
person1 = Person("Grigoriy", 77)
person2 = Person("Vasya", 11)

print(person1.name,person1.age)  
print(person2.name,person2.age)




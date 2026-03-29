class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет")
        
person1 = Person("Николай", 20)
person1.introduce()
class Mammal:
    def walk(self):
        print("walk")
        
class Dog(Mammal):
    def sound(self):
        print("woof woof")
        
class Cat(Mammal):
    def sound(self):
        print("meaw meaw")
        
class Horse(Mammal):
    pass
        
dog = Dog()
dog.walk()
dog.sound()


cat = Cat()
cat.walk()
cat.sound()
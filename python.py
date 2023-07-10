# Multilevel-inheritance.py
#Multilevel inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def give_birth(self):
        print(f"{self.name} is giving birth.")


class NonMammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")
class Cow(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def amba(self):
        print(f"{self.name} says amba.")


class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"{self.name} is barking.")


class Insect(NonMammal):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} is flying.")
# Example usage:
cow = Cow("cho cho")
cow.eat()   
cow.sleep()       
cow.give_birth()  
cow.amba()         

dog = Dog("chotu")
dog.eat()       
dog.sleep()    
dog.give_birth() 
dog.bark()        

insect = Insect("Butterfly")
insect.eat()      
insect.sleep()    
insect.lay_eggs()
insect.fly()    
#outputs
cho cho is eating.
cho cho is sleeping.
cho cho is giving birth.
cho cho says amba.
chotu is eating.
chotu is sleeping
chotu is giving birth.
chotu is barking.
Butterfly is eating.
Butterfly is sleeping.
Butterfly is laying eggs.
Butterfly is flying.



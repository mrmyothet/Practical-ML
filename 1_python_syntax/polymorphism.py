class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method 'speak'")
    
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

class Cow(Animal):
    def speak(self):
        return "Moo!"
    
class Pig(Animal):
    def speak(self):
        return "Oink!"
    
class Dino(Animal):
    def speak(self):
        return "WOOOOOO!"
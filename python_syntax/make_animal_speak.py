from polymorphism import Animal, Dog, Cat, Duck, Cow, Pig, Dino

def make_animal_speak(animal):
    """
    This function accepts any object that has a 'speak' method.
    It doesn't care about the specific type of animal, only its behavior.
    """
    print(f"{type(animal).__name__} says: {animal.speak()}")


animals_1 = [Dog(), Cat(), Duck(), Cow(), Pig()]

animals_1 = [Dog(), Cat(), Duck(), Cow(), Dino()]
for obj in animals_1:
    make_animal_speak(obj)
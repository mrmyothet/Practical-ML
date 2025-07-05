from Monster import Monster
from Dragon import Dragon

grog = Monster("Grog", 50)
blinky = Monster("Blinky", 30)

grog.take_damage(10)
blinky.take_damage(5)
print("----------")
print(f"\n{grog.name}'s final health is {grog.health}")
print(f"{blinky.name}'s final health is {blinky.health}")

smaug = Dragon("Smaug", 200)
print(smaug.health)
smaug.take_damage(25)

smaug = Dragon("Smaug", 200)
smaug.take_damage(25)

fire_damage = smaug.breathe_fire()


grog.take_damage(fire_damage)
blinky.take_damage(fire_damage)
print("----------")

print(f"The fire does {fire_damage} damage to everyone!")
print(f"{grog.name}'s final health is {grog.health}")
print(f"{blinky.name}'s final health is {blinky.health}")
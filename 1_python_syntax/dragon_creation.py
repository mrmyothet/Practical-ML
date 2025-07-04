from Dragon import Dragon

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
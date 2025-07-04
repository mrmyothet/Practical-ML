from Monster import Monster

grog = Monster("Grog", 50)
blinky = Monster("Blinky", 30)

grog.take_damage(10)
blinky.take_damage(5)
print("----------")
print(f"\n{grog.name}'s final health is {grog.health}")
print(f"{blinky.name}'s final health is {blinky.health}")
monster1 = {
  "name": "Grog",
  "health": 50,
}

def take_damage(monster, amount):
  monster["health"] -= amount
  print(f"{monster['name']} took {amount} damage!")
  print(f"It has {monster['health']} health left.")

print(f"A monster named {monster1['name']} appears with {monster1['health']} health.")
take_damage(monster1, 10)
age = 14
has_permission = True

print(f"Age: {age}, Has Parent Permission: {has_permission}")

if age >= 13 and has_permission == True:
    print("You can see the movie.")
else:
    print("Sorry, you can't see the movie.")

is_weekend = True
is_sunny = False
print(f"\n Is it the weekend? {is_weekend}, Is it sunny? {is_sunny}")

if is_weekend or is_sunny:
    print("It's a good day to play outside.")
else:
    print("Maybe stay inside and read a book.")

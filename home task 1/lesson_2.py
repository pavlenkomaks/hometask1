
import random

secret = random.randint(0, 100)

while True:
    number = int(input("Choose your nuber: "))
    if number == secret:
        print(f"You are right, this is {secret}")
        break
    elif number > secret:
        print("Too high")
    else:
        print("Too low")

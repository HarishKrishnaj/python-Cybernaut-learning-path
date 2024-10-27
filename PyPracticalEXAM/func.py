import random

def assign_value(name):
    value = random.randint(1, 50)
    print(f"The value assigned to {name} is {value}")

user_name = input("Enter your name: ")
assign_value(user_name)

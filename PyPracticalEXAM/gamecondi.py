def game():
    import random

    def get_numbers(count):
        return [random.randint(1, 100) for _ in range(count)]

    door_choice = input("Select a door (red/yellow): ").strip().lower()
    numbers_list = []

    if door_choice == "red":
        number = int(input("Select a number from 1 to 5: "))
        if number in [1, 4]:
            numbers_list = get_numbers(3)
        else:
            print("You lost")
            return
    elif door_choice == "yellow":
        number = int(input("Select a number from 6 to 10: "))
        if number % 2 == 0:
            numbers_list = get_numbers(3)
        else:
            print("You lost")
            return
    else:
        print("Invalid door choice")
        return

    total_sum = sum(numbers_list)
    if 130 < total_sum < 1079:
        print("You win")
    else:
        print("You lost")

game()

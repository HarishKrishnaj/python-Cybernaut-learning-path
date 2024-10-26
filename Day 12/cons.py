class Greeting:
    def __init__(self):
        print("Hello everyone")

    def __del__(self):
        print("Thank you")


greet = Greeting()
del greet 

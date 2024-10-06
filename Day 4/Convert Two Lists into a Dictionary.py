keys = input("Enter the keys separated by commas: ").split(',')
values = input("Enter the values separated by commas: ").split(',')
dictionary = dict(zip(keys, values))
print("The resulting dictionary is:", dictionary)

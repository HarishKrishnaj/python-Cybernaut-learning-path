set1 = set(input("Enter the elements of the first set separated by commas: ").split(','))
set2 = set(input("Enter the elements of the second set separated by commas: ").split(','))
common_elements = set1 & set2
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements found.")

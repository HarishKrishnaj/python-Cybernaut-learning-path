set1 = set(input("Enter elements of set1 separated by space: ").split())
set2 = set(input("Enter elements of set2 separated by space: ").split())
common_elements = set1.intersection(set2)
if common_elements:
    print(f"Common elements: {common_elements}")
else:
    print("No common elements found.")

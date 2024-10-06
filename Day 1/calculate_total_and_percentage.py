def calculate_total_and_percentage(marks):
    total = sum(marks)
    percentage = (total / 500) * 100
    return total, percentage
name = input("Enter student name: ")
student_class = input("Enter class: ")
section = input("Enter section: ")
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)
total, percentage = calculate_total_and_percentage(marks)
print(f"Name: {name}")
print(f"Class: {student_class}")
print(f"Section: {section}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")

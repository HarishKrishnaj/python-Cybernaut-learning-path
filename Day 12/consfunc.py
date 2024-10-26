class Student:
    count = 0  

    def __init__(self, name):
        self.name = name
        Student.count += 1
        print(f"Student's name: {self.name}")

student1 = Student("Alice")
student2 = Student("Bob")
student3 = Student("Charlie")
print(f"Number of students displayed: {Student.count}")

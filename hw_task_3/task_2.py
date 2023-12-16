class Teacher:
    def __init__(self):
        self.num_students_trained = 0

    def teach(self, material, *students):
        for student in students:
            student.take(material)
            self.num_students_trained += 1


class Student:
    def __init__(self):
        self.knowledge = []

    def take(self, material):
        self.knowledge.append(material)


class Material:
    def __init__(self, *materials):
        self.materials = list(materials)


materials = Material("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")

teacher = Teacher()

student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()

teacher.teach("Python", student1, student2)
teacher.teach("Version Control Systems", student2, student3)
teacher.teach("Relational Databases", student3, student4)
teacher.teach("NoSQL databases", student1, student4)
teacher.teach("Message Brokers", student2, student3, student4)

print("Знания ученика 1:", student1.knowledge)
print("Знания ученика 2:", student2.knowledge)
print("Знания ученика 3:", student3.knowledge)
print("Знания ученика 4:", student4.knowledge)


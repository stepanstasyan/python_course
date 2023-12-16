import random

class Human:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender


class Teacher(Human):
    def __init__(self, full_name, age, gender):
        super().__init__(full_name, age, gender)
        self.num_students_trained = 0

    def teach(self, material, *students):
        for student in students:
            student.take(material)
            self.num_students_trained += 1


class Student(Human):
    def __init__(self, full_name, age, gender):
        super().__init__(full_name, age, gender)
        self.knowledge = []

    def take(self, material):
        self.knowledge.append(material)

    def forget(self, percent_to_forget):
        if percent_to_forget < 0 or percent_to_forget > 100:
            print("Некорректное значение процента забытия. Допустимый диапазон 0-100.")
            return

        num_to_forget = int(len(self.knowledge) * percent_to_forget / 100)
        if num_to_forget > 0:
            print(f"{self.full_name} случайным образом забыл {num_to_forget} знаний.")
            self.knowledge = self.knowledge[:-num_to_forget]


class LearningMaterial:
    def __init__(self, *materials):
        self.materials = list(materials)

    def __len__(self):
        return len(self.materials)


class StudentKnowledge:
    def __len__(self):
        return len(self.knowledge)


materials = LearningMaterial("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")

teacher = Teacher("Иван Иванов", 35, "М")
student1 = Student("Алексей Иванов", 20, "М")
student2 = Student("Михаил Иванов", 22, "Ж")
student3 = Student("Игорь Иванов", 21, "М")
student4 = Student("Артем Иванов", 23, "Ж")

teacher.teach("Python", student1, student2)
teacher.teach("Version Control Systems", student2, student3)
teacher.teach("Relational Databases", student3, student4)
teacher.teach("NoSQL databases", student1, student4)
teacher.teach("Message Brokers", student2, student3, student4)

print("Знания ученика 1:", student1.knowledge)
print("Знания ученика 2:", student2.knowledge)
print("Знания ученика 3:", student3.knowledge)
print("Знания ученика 4:", student4.knowledge)

for student in [student1, student2, student3, student4]:
    student.forget(50)

print(f"\nЗнания ученика {student1.full_name} после забывания:", student1.knowledge)
print(f"Знания ученика {student2.full_name} после забывания:", student2.knowledge)
print(f"Знания ученика {student3.full_name} после забывания:", student3.knowledge)
print(f"Знания ученика {student4.full_name} после забывания:", student4.knowledge)

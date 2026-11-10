class Department:
    def __init__(self, name: str):
        self.name = name
        self.courses = {}  #дисциплина: специальности

    def add_discipline(self, discipline_name: str, specialties: list):
        self.courses[discipline_name] = specialties

    def can_teach(self, discipline_name: str, specialty: str):
        if discipline_name in self.courses:
            return specialty in self.courses[discipline_name]
        return False


class Student:
    def __init__(self, id: int, name: str, specialty: str, semester: int = 1):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.semester = semester
        self.disciplines = {} #дисциплина: оценка

    def add_discipline(self, discipline_name: str):
        self.disciplines[discipline_name] = None

    def remove_discipline(self, discipline_name: str):
        if discipline_name in self.disciplines:
            del self.disciplines[discipline_name]

    def set_grade(self, discipline_name: str, grade: int):
        self.disciplines[discipline_name] = grade

    def get_average_grade(self):
        grades = [grd for grd in self.disciplines.values()]
        try:
            return sum(grades) / len(grades)
        except ZeroDivisionError:
            print("Деление на ноль")

    def can_transfer(self):
        if not self.disciplines:
            return False
        for grade in self.disciplines.values():
            if grade is None or grade < 4:
                return False
        return True


class Faculty:
    def __init__(self, name: str):
        self.name = name
        self.departments :list[Department] = []
        self.students :dict[int,Student]= {}

    def add_department(self, department: Department):
        self.departments.append(department)

    def find_reading_department(self, discipline_name: str, specialty: str):
        for department in self.departments:
            if department.can_teach(discipline_name, specialty):
                return department
        return None

    def add_student(self, student_id: int, name: str, specialty: str):
        if student_id in self.students:
            print("Студент с таким ID уже существует")
        else:    
            student = Student(student_id, name, specialty)
            self.students[student_id] = student
            return student

    def remove_student(self, student_id: int):
        return self.students.pop(student_id)

    def add_student_to_discipline(self, student_id: int, discipline_name: str):

        student = self.students[student_id]

        department = self.find_reading_department(discipline_name, student.specialty)
        if not department:
            print(f"Дисциплина '{discipline_name}' не ведется для специальности '{student.specialty}'")

        if discipline_name in student.disciplines:
            print(f"Студент уже изучает дисциплину '{discipline_name}'")

        student.add_discipline(discipline_name)

    def remove_student_from_discipline(self, student_id: int, discipline_name: str):

        student = self.students[student_id]

        if discipline_name not in student.disciplines:
            print(f"Студент не записан на дисциплину '{discipline_name}'")
        else:
            student.remove_discipline(discipline_name)

    def set_grade(self, student_id: int, discipline_name: str, grade: int):

        student = self.students[student_id]

        if discipline_name not in student.disciplines:
            print(f"Студент не записан на курс '{discipline_name}'")

        if not (1 <= grade <= 10):
            print("Некорректная оценка (оценка должна быть от 1 до 10)")

        student.set_grade(discipline_name, grade)

    def transfer_student(self, student_id: int):

        student = self.students[student_id]

        if not student.can_transfer():
            print("Нельзя перевести студента: есть несданные дисциплины или задолженности (оценка ниже 4)")

        student.semester += 1
        student.disciplines.clear()
        return student.semester

    def save_student_report(self, student_id: int):

        student = self.students[student_id]

        filename = f"report_student_{student.id}.txt"
        avg_grade = student.get_average_grade()

        lines = [
            "Ведомость успеваемости студента",
            f"ID: {student.id}",
            f"ФИО: {student.name}",
            f"Специальность: {student.specialty}",
            f"Семестр: {student.semester}",
            f"Средний балл: {avg_grade}",
            "Дисциплины:"
        ]
        if not student.disciplines:
            lines.append("(нет изучаемых дисциплин)")
        else:
            for discipline, grade in student.disciplines.items():
                department = self.find_reading_department(discipline, student.specialty)
                department_name = department.name if department else "Не указана"
                grade_str = str(grade) if grade is not None else "нет оценки"
                lines.append(f"  - {discipline} (Кафедра: {department_name}): {grade_str}")

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("\n".join(lines) + "\n")
        return filename


#########
faculty = Faculty("РАФ")

dep1 = Department("Кафедра САиКМ")
dep1.add_discipline("Базы данных", ["прикладная информатика"])

dep2 = Department("Кафедра КФС")
dep2.add_discipline("чтото", ["прикладная информатика"])


faculty.add_department(dep1)
faculty.add_department(dep2)

faculty.add_student(1, "Синоженский", "прикладная информатика")

operations = {
    1: ":Записать на дисциплину",
    2: ":Удалить из дисциплины",
    3: ":Выставить оценку",
    4: ":Перевести в следующий семестр",
    5: ":Сформировать ведомость в файл",
    6: ":Отчислить студента",
    0: ":Выход"
    }

while True:
    print("\nСписок команд")
    student_id_input = input("Введите ID студента (или 0 для выхода): ")
    if student_id_input == "0":
        break

    try:
        student_id = int(student_id_input)
    except ValueError:
        print("Некорректный ID! Введите число.")
        continue

    if student_id not in faculty.students:
        print("Студент с таким ID не найден.")
        choice = input("Зачислить нового студента? (1 - да, 0 - нет): ")
        if choice == "1":
            name = input("Введите имя студента: ")
            specialty = input("Введите специальность: ")
            
            faculty.add_student(student_id, name, specialty)
            print(f"Студент {name} успешно зачислен.")

        else:
            continue

    while True:
        student = faculty.students.get(student_id)
        if not student:
            break

        print(f"\nСтудент: {student.name} (ID: {student.id}, Специальность: {student.specialty}, Семестр: {student.semester}) ")
        for key, text in operations.items():
            print(key, text)

        try:
            choice = int(input("Выберите действие: "))
        except ValueError:
            print("Неверная команда")
            continue

        if choice == 1:
            discipline = input("Введите название дисциплины: ")
            faculty.add_student_to_discipline(student_id, discipline)

        elif choice == 2:
            discipline = input("Введите название дисциплины: ")
            faculty.remove_student_from_discipline(student_id, discipline)

        elif choice == 3:
            discipline = input("Введите название дисциплины: ")
            grade = int(input("Введите оценку (от 1 до 10): "))
            faculty.set_grade(student_id, discipline, grade)

        elif choice == 4:
            new_semester = faculty.transfer_student(student_id)

        elif choice == 5:
            filename = faculty.save_student_report(student_id)
            print(f"Ведомость успешно сохранена в файл: {filename}")
        
        elif choice == 6:
            faculty.remove_student(student_id)
            print(f"Студент {student.name} отчислен.")
            break
            
        elif choice == 0:
            break
        else:
            print("Неверная команда")




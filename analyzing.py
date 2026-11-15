import numpy as np

students = [f"Студент {i}" for i in range(1, 23)]
subjects = ["Джавка", "Числаки", "ТВиМС", "Python", "Диффуры"]

grades = np.random.randint(3, 11, size=(len(students), len(subjects))) #строки студенты, столбцы преметы

print("Таблица оценок:")
print(grades)
print("-" * 40)

student_avg = np.mean(grades, axis=1)

for i in range(len(students)):
    print(f"{students[i]}: оценки {grades[i]} средний балл: {student_avg[i]}")

print("-" * 40)

best = np.argmax(student_avg)
worst = np.argmin(student_avg)

print(f"Лучший студент: {students[best]} ({student_avg[best]})")
print(f"Худший студент: {students[worst]} ({student_avg[worst]})")

print("-" * 40)

subject_avg = np.mean(grades, axis=0)

for i in range(len(subjects)):
    print(f"{subjects[i]}: средний балл {subject_avg[i]}")

easiest = np.argmax(subject_avg)
hardest = np.argmin(subject_avg)

print(f"\nСамый простой предмет: {subjects[easiest]} ({subject_avg[easiest]})")
print(f"Самый сложный предмет: {subjects[hardest]} ({subject_avg[hardest]})")

print("-" * 40)

coeffs = np.zeros(len(students))
base_stipend = 270

for i in range(len(students)):
    if np.min(grades[i]) >= 4:
        if student_avg[i] >= 9:
            coeffs[i] = 1.6 
        elif student_avg[i] >= 8:
                    coeffs[i] = 1.33       
        elif student_avg[i] >= 6:
            coeffs[i] = 1.2  

if np.sum(coeffs) > 0:
    stipends = coeffs * base_stipend
else:
    stipends = np.zeros(len(students))

print("Распределение стипендии:")
for i in range(len(students)):
    print(f"{students[i]}: {stipends[i]} руб.")
list1 = input("Введите первый набор чисел через пробел: ").split()
list2 = input("Введите второй набор чисел через пробел: ").split()

set1 = set(list1)
set2 = set(list2)

intersection = set1 & set2

only_in_first = set1 - set2
only_in_second = set2 - set1
all_without_intersection = (set1|set2)- intersection

print("\n--- Результаты сравнения ---")
print(f"1. Присутствуют в обоих наборах: {intersection}")
print(f"2. Присутствуют только в первом наборе: {only_in_first}")
print(f"   Присутствуют только во втором наборе: {only_in_second}")
print(f"3. Все числа, за исключением общих (симметрическая разность): {all_without_intersection}")
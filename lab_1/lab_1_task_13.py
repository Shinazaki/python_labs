input = input("Введите числа через пробел: ").split()
numbers = []
float_numbers = []

for number in input:
    if "." in number:
        val = float(number)
        float_numbers.append(val)
    else:
        val = int(number)
    numbers.append(val)

counts = {}
for num in numbers:
    counts[num] = counts.get(num, 0) + 1

unique_numbers = [num for num, count in counts.items() if count == 1]

duplicate_numbers = [num for num, count in counts.items() if count > 1]

even_numbers = []
odd_numbers = []
for num in numbers:
    if isinstance(num, int) or num.is_integer():
        int_val = int(num)
        if int_val % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

negative_numbers = [num for num in numbers if num < 0]

sum_divisible_by_5 = 0
for num in numbers:
    if (isinstance(num, int) or num.is_integer()) and int(num) % 5 == 0:
        sum_divisible_by_5 += num

max_num = numbers[0]
min_num = numbers[0]
for num in numbers[1:]:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"1. Уникальные числа: {unique_numbers}")
print(f"2. Повторяющиеся числа: {duplicate_numbers}")
print(f"3. Четные числа: {even_numbers}")
print(f"   Нечетные числа: {odd_numbers}")
print(f"4. Отрицательные числа: {negative_numbers}")
print(f"5. Числа с плавающей точкой: {float_numbers}")
print(f"6. Сумма всех чисел, кратных 5: {sum_divisible_by_5}")
print(f"7. Самое большое число: {max_num}")
print(f"8. Самое маленькое число: {min_num}")
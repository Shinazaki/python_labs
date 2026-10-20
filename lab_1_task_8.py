import random
number_to_guess = random.randint(1,100)
user_guess = -1
while user_guess != number_to_guess:
    user_guess = int(input("Введите число: "))
    if user_guess > number_to_guess:
        print(f"Число {user_guess} больше загаданного\n")
        continue
    if user_guess < number_to_guess:
        print(f"Число {user_guess} меньше загаданного\n")
        continue
print("Число угадано")    
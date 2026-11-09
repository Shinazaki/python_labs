"""Создпём фитнесс трекер. Пользователь вводит еду и кол-во калорий и вводит упражнения и кол-во каллрий потрачено за упражнение
создать при помощи декоратора сообщение о том сколько каллорий нужно потратить (2500ккал норма) и должен быть создан файл"""

def report(count,count_ex):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            odd_callories = count - count_ex
            print (count,count_ex)
            if odd_callories < 2500:
                print("Всё в норме ")
                callories_to_burn = odd_callories - 2500    
            else:
                print(f"Вам нужно потратить ещё {callories_to_burn} ккал.")
            with open("outpur.txt",mode="w",encoding="utf-8") as file:
                file.write(f"Кол-во каллорий за всю съеденную еду {count} ккал.\n")
                file.write(f"Кол-во каллорий за все выполнненые упражнения {count_ex} ккал.\n")
                file.write(f"Сколько ещё нужно сжечь каллоррий {callories_to_burn}\n")
            return result
        return wrapper
    return decorator




food_and_callories = {}
exercises_and_callories = {}

while True:
    food = input("Введите еду(или 0 для выхода из программы и рассчётов): ")
    if food == "0":
        break
    callories = input(f"Введите кол-во калорий для {food}: \n")
    try:
        food_and_callories[food] = int(callories)
    except ValueError:
        print("Неверно введены данные\n")    

count = 0
print()
for callories in food_and_callories.values():
    count += callories

while True:
    exercise = input("Введите упражнение(или 0 для выхода из программы и рассчётов): ")
    if exercise == "0":
        break
    callories_ex = input(f"Введите кол-во калорий для {exercise}: \n")
    try:
        exercises_and_callories[exercise] = int(callories_ex)
    except ValueError:
        print("Неверно введены данные\n")        

count_ex = 0
print()

for callories in exercises_and_callories.values():
    count_ex += callories

@report(count,count_ex)
def print_info(count,count_ex):
    return f"Вы съели {count} ккал. вы потратили {count_ex} ккал."

print_info(count,count_ex)
sum_of_purchase = int(input("Введите сумму покупки: "))
age_of_customer = int(input("Введите возраст: "))
is_date_of_birth = int(input("Есть ли день рождения(Введите 0 - если нет, 1 - если да): "))
assert is_date_of_birth in [0,1], "Некоректные данные для дня рождения"

is_VIP = int(input("Есть ли VIP статус(Введите 0 - если нет, 1 - если да): "))
assert is_VIP in [0,1], "Некоректные данные для VIP статуса"

discount = 0
if sum_of_purchase > 1000:
    discount += 10
if age_of_customer >=63:
    discount += 5
if bool(is_date_of_birth):
    discount += 5
if bool(is_VIP):
    if sum_of_purchase > 1000:
        discount +=5
    else:
        discount+=15
            

if discount > 25:
    discount = 25

print(f"Итоговая скидка: {discount}")    
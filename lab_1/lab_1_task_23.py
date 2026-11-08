income = float(input("Введите общий доход за месяц в рублях: "))

categories = ["Жилье", "Питание", "Транспорт", "Развлечения", "Прочее"]
expenses = {}

print("\nВведите расходы по категориям")
for cat in categories:
    expenses[cat] = float(input(f"{cat}: "))

total_expense = sum(expenses.values())
savings = income - total_expense
savings_rate = (savings / income * 100) if income > 0 else 0

print("\n" + "=" * 30)
print(f"Всего расходов: {total_expense} руб.")
print(f"Остаток: {savings} руб. ({savings_rate}% дохода)")

print("\nДоли расходов:")
for cat, amount in expenses.items():
    pct = (amount / total_expense * 100) if total_expense > 0 else 0
    print(f"{cat}: {amount} руб. ({pct}%)")


print("Рекомендации:", end = "")
if savings < 0:
    print("Расходы превышают доходы, сократите траты на развлечения.")
elif savings_rate < 20:
    print("Норма сбережений ниже нормы, попробуйте урезать второстепенные расходы.")
else:
    print("Отличный баланс")

top_cat = max(expenses, key=expenses.get)
print(f"Главная статья расходов {top_cat}.")

print("Планирование крупной покупки")
goal_name = input("На что хотите накопить? ")
goal_cost = float(input("Сколько это стоит (руб)? "))

if savings > 0:
    months = goal_cost / savings
    print(f"При текущих сбережениях вы накопите на '{goal_name}' за {months} мес.")
else:
    print(f"Вы не откладываете деньги, накопить на '{goal_name}' сейчас невозможно.")
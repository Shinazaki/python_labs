import numpy as np

def age_rate_calculate(age: int) -> float:
    gradation = (
        (18,0.0),
        (21,0.2),
        (34,0.6),
        (50,1.0),
        (65,0.7),
        (75,0.3)
    )
    for max_age,rating in gradation:
        if age <= max_age:
            return rating
    return 0.0

def risk_rate_calculation(risk_rate: float) -> int:
    gradation = (
        (25,0),
        (50,1),
        (75,2),
        (100,3)
    )
    for max_risk,rating in gradation:
            if risk_rate*100 <= max_risk:
                return rating
    return 3.0

age_rate = age_rate_calculate(int(input("Введите свой возраст: ")))

earnings = int(input("Введите ежемясячный доход в руб: "))

sum_of_credit = int(input("Введите сумму запрашиваемого кредита: "))

time_of_credit = int(input("Введите срок кредита в месяцах: "))

credit_history = int(input("Введите кредитную историю от 0 до 3, где 3 - отличная 2 - хорошая 1 - удовлетворительная 0 - плохая: "))
assert credit_history in [0,1,2,3], "Неккоректные данные"

is_guaranted = int(input("Введите есть ли у вас поручитель, где 0 - нет 1 - да: "))
assert is_guaranted in [0,1], "Неккоректные данные"

is_deposit = int(input("Введите есть ли у вас залог, где 0 - нет 1 - да: "))
assert is_deposit in [0,1], "Неккоректные данные"

relationship = earnings/sum_of_credit
if relationship != 0:
    print(f"соотношение кредита к доходу: {1/relationship}")
else:    
    print(f"соотношение кредита к доходу: 0")
#Первая точка выхода
inputs = np.array([age_rate,relationship,time_of_credit,credit_history,is_guaranted,is_deposit])
risk_weights = np.array([0.05,
                         0.25 if relationship < 1 else -0.25,
                         0.15,
                         -0.3,
                         -0.1,
                         -0.15]).T
risk_rate = risk_rate_calculation(inputs.dot(risk_weights))
print(f"Категория риска: {risk_rate}")

#
base_rate = 15.0  
category = {0: 0.0, 1: 3.0, 2: 7.0, 3: 12.0}
addition_percent = base_rate + category[risk_rate]

print(f"Рекомендуемая ставка: {addition_percent:}% годовых")

#
if risk_rate >=2:
     print(f"Следует отказать в кредите")
else:
     print(f"Следует одобрить кредит")   
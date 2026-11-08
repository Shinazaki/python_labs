def convert_temperature(val: float, from_unit: str, to_unit: str) -> float:
    #в цельсии
    if from_unit == "c":
        celsius = val
    elif from_unit == "f":
        celsius = (val - 32) * 5 / 9
    elif from_unit == "k":
        celsius = val - 273.15
    else:
        assert False,"неверная единицв"
    #из цельсий
    if to_unit == "c":
        return celsius
    elif to_unit == "f":
        return celsius * 9 / 5 + 32
    elif to_unit == "k":
        return celsius + 273.15
    else:
        assert False,"неверная единицв"



categories = {
    1: {
        "name": "Длина (базовая: метр)",
        "units": {
            "мм": 0.001,
            "см": 0.01,
            "м": 1.0,
            "км": 1000.0,
            "дюйм": 0.0254,
            "фут": 0.3048,
        },
    },
    2: {
        "name": "Масса (базовая: килограмм)",
        "units": {
            "г": 0.001,
            "кг": 1.0,
            "т": 1000.0,
            "фунт": 0.453592,
            "унция": 0.0283495,
        },
    },
    3: {
        "name": "Температура",
        "units": {
            "c": "Градусы Цельсия (°C)",
            "f": "Градусы Фаренгейта (°F)",
            "k": "Кельвины (K)",
        },
    },
    
}

print("Выберите тип измерения:")
for key, data in categories.items():
    print(f"  {key}. {data['name']}")

choice = int(input("\nВведите номер категории: "))

assert not(choice not in categories), "неправильный выбор"

category = categories[choice]
available_units = category["units"]

print(f"\nДоступные единицы: {', '.join(available_units.keys())}")

from_unit = input("Введите исходную единицу: ").lower()
to_unit = input("Введите целевую единицу: ").lower()

assert not(from_unit not in available_units or to_unit not in available_units), "Неправильные вхожные данные"

try:
    value = float(input("Введите значение для перевода: ").replace(",", "."))
except ValueError:
    print("Ошибка: введено некорректное число!")

if choice == "3":  
    result = convert_temperature(value, from_unit, to_unit)
else:  
    base_value = value * available_units[from_unit]
    result = base_value / available_units[to_unit]

print(f"\nРезультат: {value} {from_unit} = {result:.4f} {to_unit}")


import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate, optimize, integrate

hours_raw = np.array([0, 2, 3, 6, 8, 11, 13, 15, 18, 20, 23])
temp_raw = np.array([15.2, 14.5, 14.1, 15.8, 18.4, 22.9, 25.6, 26.1, 23.4, 20.1, 16.5])

f_temp = interpolate.CubicSpline(hours_raw, temp_raw)

all_hours = np.arange(0, 24)
hourly_temp = f_temp(all_hours)

print("Восстановленная температура по часам:")
for h, t in zip(all_hours, hourly_temp):
    print(f"{h}:00 -> {float(t)} °C")

print("-" * 45)

res_min = optimize.minimize_scalar(f_temp, bounds=(0, 23), method="bounded")
min_time = res_min.x
min_temp = res_min.fun

res_max = optimize.minimize_scalar(lambda x: -f_temp(x), bounds=(0, 23), method="bounded")
max_time = res_max.x
max_temp = -res_max.fun

def format_time(hours_float):
    h = int(hours_float)
    m = int((hours_float - h) * 60)
    if m == 60:
        h += 1
        m = 0
    return f"{h}:{m}"

print(f"Самая низкая температура: {float(min_temp)} °C в {format_time(min_time)}")
print(f"Самая высокая температура: {float(max_temp)} °C в {format_time(max_time)}")

integral_value, _ = integrate.quad(f_temp, 0, 23)
avg_temp = integral_value / 23

print(f"Средняя температура за день: {avg_temp} °C")

norm_temp = 22.0
crossings = []

for i in range(len(all_hours) - 1):
    t1, t2 = all_hours[i], all_hours[i + 1]
    if (f_temp(t1) - norm_temp) * (f_temp(t2) - norm_temp) <= 0:
        root = optimize.root_scalar(lambda x: f_temp(x) - norm_temp, bracket=[t1, t2])
        if root.converged:
            crossings.append(root.root)

print("Пересечение порога 22 °C произошло в:")
for t in crossings:
    print(f" - {format_time(t)} ч")

t_smooth = np.linspace(0, 23, 300)

plt.plot(t_smooth, f_temp(t_smooth), label="Функция температуры от времени", color="blue", linewidth=2)
plt.scatter(hours_raw, temp_raw, color="black", zorder=5, label="Исходные данные датчика")

plt.scatter(min_time, min_temp, color="yellow", s=80, zorder=6, label=f"Минимум: {min_temp}°C ({format_time(min_time)})")
plt.scatter(max_time, max_temp, color="red", s=80, zorder=6, label=f"Максимум: {max_temp}°C ({format_time(max_time)})")

plt.axhline(norm_temp, color="green", linestyle="--", label="Норма (22 °C)")
if crossings:
    plt.scatter(crossings, [norm_temp] * len(crossings), color="green", s=60, zorder=6, label="Пересечение нормы")

plt.title("Температура воздуха в теплице за сутки")
plt.xlabel("Время суток (часы)")
plt.ylabel("Температура (°C)")
plt.xticks(range(0, 24))
plt.grid(True, linestyle="-", alpha=0.7)
plt.legend()
plt.show()
import pandas as pd
import plotly.express as px

pd.set_option('future.no_silent_downcasting', True)
df = pd.read_csv("genshin.csv", encoding="latin1")

print("=" * 60)
print("1. ИЗУЧЕНИЕ ДАННЫХ И ОПИСАТЕЛЬНАЯ СТАТИСТИКА")
print("=" * 60)

print(f"Размерность датасета: {df.shape[0]} строк, {df.shape[1]} столбцов\n")

print("Первые 5 строк датасета:")
print(df[["character_name", "rarity", "region", "vision", "weapon_type", "hp_90_90", "atk_90_90", "def_90_90"]].head())
print("-" * 50)

print("Типы данных (основные столбцы):")
print(df.dtypes.head(20))
print("-" * 50)

print("Описательная статистика числовых характеристик:")
print(df[["hp_90_90", "atk_90_90", "def_90_90"]].describe())
print("-" * 50)

print("\n" + "=" * 60)
print("2. ОБРАБОТКА ПРОПУСКОВ И ДУБЛИКАТОВ")
print("=" * 60)

null_counts = df.isnull().sum()
cols_with_nulls = null_counts[null_counts > 0]
print("Число пропущенных значений по столбцам:")
print(cols_with_nulls)
print("-" * 50)

for col in df.select_dtypes(include=["number"]).columns:
    if df[col].isnull().any():
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

for col in df.select_dtypes(include=["object", "string"]).columns:
    if df[col].isnull().any():
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)

print(f"Осталось пропущенных значений после заполнения: {df.isnull().sum().sum()}")
print("-" * 50)

duplicates_count = df.duplicated().sum()
print(f"Количество полных дубликатов строк: {duplicates_count}")
if duplicates_count > 0:
    df = df.drop_duplicates()
    print("Дубликаты успешно удалены.")
print("-" * 50)

print("\n" + "=" * 60)
print("3. СОЗДАНИЕ НОВЫХ ЧИСЛОВЫХ СТОЛБЦОВ")
print("=" * 60)

df["Total_stats_at_90_lvl"] = df["hp_90_90"] + df["atk_90_90"] + df["def_90_90"]

df["Atk_def_relationship"] = (df["atk_90_90"] / df["def_90_90"]).round(2)

print("Созданы столбцы 'Total_stats_at_90_lvl' и 'Atk_def_relationship'. Пример данных:")
print(df[["character_name", "hp_90_90", "atk_90_90", "def_90_90", "Total_stats_at_90_lvl", "Atk_def_relationship"]].head())
print("-" * 50)


print("\n" + "=" * 60)
print("4. МАТРИЦА КОРРЕЛЯЦИИ")
print("=" * 60)

corr_columns = ["rarity", "hp_90_90", "atk_90_90", "def_90_90", "Total_stats_at_90_lvl", "Atk_def_relationship"]
corr_matrix = df[corr_columns].corr()
print(corr_matrix.round(3))
print("-" * 50)

print("\n" + "=" * 60)
print("5. АНАЛИЗ ПО ГЛАВНОМУ КАТЕГОРИАЛЬНОМУ ПРИЗНАКУ (РЕГИОН)")
print("=" * 60)

region_stats = df.groupby("region")["atk_90_90"].agg(
    count="count",
    mean="mean",
    median="median"
).round(2).reset_index()

print("Количество записей, среднее и медиана базовой атаки по регионам:")
print(region_stats)
print("-" * 50)

print("\n" + "=" * 60)
print("6. СВОДНАЯ ТАБЛИЦА")
print("=" * 60)

pivot_table = pd.pivot_table(
    df,
    values="atk_90_90",
    index="region",
    columns="weapon_type",
    aggfunc="mean"
).round(1)

print("Сводная таблица средней силы атаки (Регион x Оружие):")
print(pivot_table)
print("-" * 50)

print("\n" + "=" * 60)
print("7. ТОП-5 ПЕРСОНАЖЕЙ (ФИЛЬТР: ТОЛЬКО 5★ ПЕРСОНАЖИ)")
print("=" * 60)

df_five_star = df[df["rarity"] == 5]

top_5_atk = df_five_star.nlargest(5, "atk_90_90")[["character_name", "region", "vision", "weapon_type", "atk_90_90"]]
worst_5_atk = df_five_star.nsmallest(5, "atk_90_90")[["character_name", "region", "vision", "weapon_type", "atk_90_90"]]

print("Топ-5 лучших 5★ персонажей по базовой атаке:")
for i, row in enumerate(top_5_atk.itertuples(), 1):
    print(f"{i}. {row.character_name} ({row.region}, {row.vision}, {row.weapon_type}) — ATK: {row.atk_90_90}")

print("-" * 50)
print("Топ-5 худших 5★ персонажей по базовой атаке:")
for i, row in enumerate(worst_5_atk.itertuples(), 1):
    print(f"{i}. {row.character_name} ({row.region}, {row.vision}, {row.weapon_type}) — ATK: {row.atk_90_90}")
print("-" * 50)

TEMPLATE = "plotly_white"

pivot_melted = pivot_table.reset_index().melt(
    id_vars="region",
    var_name="weapon_type",
    value_name="avg_atk"
).dropna()

fig_bar = px.bar(
    pivot_melted,
    x="region",
    y="avg_atk",
    color="weapon_type",
    barmode="group",
    text_auto=".1f",
    title="Сравнение средней базовой атаки по регионам и типам оружия",
    labels={
        "region": "Регион",
        "avg_atk": "Средняя базовая атака (90 ур.)",
        "weapon_type": "Тип оружия"
    },
    template=TEMPLATE
)
fig_bar.update_layout(xaxis_title="Регион", yaxis_title="Средняя базовая атака")

fig_box = px.box(
    df,
    x="region",
    y="atk_90_90",
    color="region",
    points="all",
    title="Распределение базовой силы атаки персонажей по регионам",
    labels={
        "region": "Регион",
        "atk_90_90": "Базовая атака (90 ур.)"
    },
    template=TEMPLATE
)
fig_box.update_layout(xaxis_title="Регион", yaxis_title="Базовая атака (90 ур.)")

fig_scatter = px.scatter(
    df,
    x="hp_90_90",
    y="atk_90_90",
    color="region",
    hover_name="character_name",
    trendline="ols",
    title="Диаграмма рассеяния: зависимость между HP и силой атаки с линией тренда",
    labels={
        "hp_90_90": "Базовое здоровье (HP 90 ур.)",
        "atk_90_90": "Базовая атака (ATK 90 ур.)",
        "region": "Регион"
    },
    template=TEMPLATE
)
fig_scatter.update_layout(xaxis_title="Базовое здоровье (HP 90 ур.)", yaxis_title="Базовая атака (ATK 90 ур.)")

fig_heatmap = px.imshow(
    pivot_table,
    text_auto=".1f",
    aspect="auto",
    color_continuous_scale="Viridis",
    title="Тепловая карта средней базовой атаки (Регион x Тип оружия)",
    labels=dict(x="Тип оружия", y="Регион", color="Средняя атака"),
    template=TEMPLATE
)
fig_heatmap.update_layout(xaxis_title="Тип оружия", yaxis_title="Регион")

fig_bar.show()
fig_box.show()
fig_scatter.show()
fig_heatmap.show()
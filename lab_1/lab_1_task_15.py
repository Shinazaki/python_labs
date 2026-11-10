sales_data = [
    {"name": "Ноутбук", "price": 50000, "quantity": 3},
    {"name": "Смартфон", "price": 25000, "quantity": 5},
    {"name": "Наушники", "price": 3000, "quantity": 10},
    {"name": "Ноутбук", "price": 50000, "quantity": 2},  
    {"name": "Мышь", "price": 1500, "quantity": 8},
    {"name": "Смартфон", "price": 25000, "quantity": 1},
]


if not sales_data:
    assert False, "Список продаж пуст."

revenue_by_product = {}

for item in sales_data:
    name = item["name"]
    revenue = item["price"] * item["quantity"]
    revenue_by_product[name] = revenue_by_product.get(name, 0) + revenue

top_product = max(revenue_by_product, key=revenue_by_product.get)
max_revenue = revenue_by_product[top_product]

unique_count = len(revenue_by_product)

print(f"Самый прибыльный товар: {top_product}")
print(f"Количество уникальных наименований: {unique_count}")

"""dictionary"""

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

total_category = {}

for element in products:
    cate = element["category"]
    price = element["price"]
    total_category[cate] = total_category.get(cate, 0) + price

print(total_category)
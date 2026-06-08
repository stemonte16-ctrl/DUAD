"""dictionary"""

sales = [
    {
        "date" : "27/02/23",
        "customer_email" : "joe@mail.com",
        "items" : [
            {
                "name" : "Lava Lamp",
                "upc" : "ITEM-453",
                "unit_price" : 65.76,
            },
            {
                "name" : "Iron",
                "upc" : "ITEM-324",
                "unit_price" : 32.45,
            },
            {
                "name" : "Basketball",
                "upc" : "ITEM-432",
                "unit_price" : 12.54,
            },
        ],
    },
    {
        "date" : "27/02/23",
        "customer_email": "david@gmail.com",
        "items" : [
            {
                "name" : "Lava Lamp",
                "upc" : "ITEM-453",
                "unit_price" : 5.42,
            },
            {
                "name" : "Key Holder",
                "upc" :"ITEM-23",
                "unit_price" : 5.42
            }
        ],
    },
    {
        "date" : "26/02/23",
        "customer_email" : "amanda@gmail.com",
        "items" : [
            {
                "name" : "Key Holder",
                "upc" : "ITEM-23",
                "unit_price" : 17.54,
            }
        ],
    },
]

result = {}

for venta in sales:
    for item in venta["items"]:
        upc = item["upc"]
        price = item ["unit_price"]
        result[upc] = result.get(upc, 0) + price

print(result)
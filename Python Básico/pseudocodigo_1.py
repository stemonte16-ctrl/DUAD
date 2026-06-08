"""pseudocode"""

price = float(input("Enter the price: "))
discount = 0
final_price = 0

if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10

final_price = price - discount
print(final_price)

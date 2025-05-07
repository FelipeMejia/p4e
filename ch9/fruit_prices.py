fruit_prices = {"watermelon": 2, "apple": 0.5, "banana": 0.25}
fruit_keys = fruit_prices.keys()
fruit_values = fruit_prices.values()

print(list(fruit_keys))
print(list(fruit_values))

for fruit, price in fruit_prices.items():
    print(fruit, price)

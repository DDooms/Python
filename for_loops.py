for price in 'Python':
    print(price)

for price in range(50, 100, 2):  # begin, end, steps
    print(price)

# shopping cart
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price

print(f'Total is {total}')

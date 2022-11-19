numbers = range(1, 101)

even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared_numbers = map(lambda x: x ** 2, even_numbers)

print(f'Squared even numbers: {list(squared_numbers)}')

# [f(item) for item in collection if p(item)] -> syntax for list comprehension

print(f'Squared even numbers: {[x ** 2 for x in range(1, 101) if x % 2 == 0]}')

numbers = [1, 2, 3]
print(f'Odd numbers: {[number for number in numbers if number % 2 != 0]}')
print(f'Multiplying all numbers by 2: {[number * 2 for number in numbers]}')


def calculate_area_of_rectangle(a, b):
    return a * b


rectangles = [(1, 2), (5, 4), (3, 2.5), (-2, 3)]
areas = [calculate_area_of_rectangle(x, y) for x, y in rectangles if x >= 0 and y >= 0]

print(f'Areas of valid rectangles: {areas}')

numbers = [7, 12, 5, 6, 9, 15, 1, 11]

results = ["Yes" if number % 3 == 0 or number % 5 == 0 else "No" for number in numbers]
# ternary operator

print(f'Results are: {results}')

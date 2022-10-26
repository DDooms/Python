names = ['John', 'Bob', 'Mosh', 'Sarah']
numbers = [3, 6, 7, 8, 3, 1, 2, 0, 5]
numbers.append(20)
numbers.insert(3, 10)
numbers.remove(20)
print(max(numbers))
numbers.clear()

# 2d lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)

# remove duplicates in a list
lists = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in lists:
    if number not in uniques:
        uniques.append(number)

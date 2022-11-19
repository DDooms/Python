def multiply_by_two(number):
    return number * 2


def my_map(map_function, collection):
    result = []

    for item in collection:
        result.append(map_function(item))

    return result


numbers = [2, 7, 3, 9, -1, 12]
print(f'Squared numbers: {my_map(multiply_by_two, numbers)}')

numbers = [1, 2, 3, 4]

mapped_numbers = map(lambda number: number ** 2, numbers)
result2 = list(mapped_numbers)

print(result2)

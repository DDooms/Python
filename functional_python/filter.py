numbers = [2, 7, 11, 12]


def is_even(number):
    return number % 2 == 0


def my_filter(filter_fn, collection):
    result = []
    for item in collection:
        if filter_fn(item):
            result.append(item)

    return result


print(my_filter(is_even, numbers))
print(list(filter(is_even, numbers)))
print(list(filter(lambda number: number % 2 == 0, numbers)))

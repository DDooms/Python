from functools import reduce

numbers = [3, 5, 8]


def multiply(a, b):
    return a * b


print(reduce(multiply, numbers, 1))
#  first reduce, it takes the function, the collection, and the amount you want to apply to it

print(reduce(lambda acc, number: acc * number, numbers, 1))
# lambda takes 2 arguments: accumulate and number. 1 is the value of the acc and everytime is multiplied by the
# number. Numbers is the collection

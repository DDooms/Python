from itertools import zip_longest

first_numbers = [1, 2, 3, 4]
second_numbers = [5, 6, 7, 8]

print(zip(first_numbers, second_numbers))
print(list(zip(first_numbers, second_numbers)))  # returns tuples

names = ['Иван', 'Любо', 'Алекс']
favorite_number = [3, 20, 8]

print(list(zip(names, favorite_number)))  # lists can be of different types

names = ['Иван', 'Любо', 'Алекс', 'Иво']
favorite_number = [3, 20, 7]

print(list(zip(names, favorite_number)))  # if one list is longer than the other one, it gets cut

names = ['Иван', 'Любо', 'Алекс']
favorite_number = [3, 20, 7, -1]

zip(names, favorite_number, strict=True)  # if that is the case, with strict=True, python will throw exception

names = ['Иван', 'Любо', 'Алекс']
favorite_number = [3, 20, 7, -1, -2]

print(list(zip_longest(names, favorite_number, fillvalue='Dummy')))
# with fillvalue, we can fill the empty spaces, without a need of an exception

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

print(list(zip(map(lambda x: x ** 2, numbers), letters)))
# [(1, 'a'), (4, 'b'), (9, 'c')]

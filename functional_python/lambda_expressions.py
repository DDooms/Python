print((lambda x: x + 2)(5))
f = lambda y: y + 3
z = lambda y, x: y + x
print(f(7))
print(z(7, 10))

list_ = [1, 4, 8, 1, 3, 5]
list_.sort(key=lambda ascending: ascending)
list_.sort(key=lambda descending: -descending)
print(list_)

people_data = [('Beray', 22), ('Edis', 71), ('John', 35), ('Somebody', 51), ('Al-Haitham', 35)]
people_data.sort(key=lambda ascending_age: ascending_age[1])
people_data.sort(key=lambda ascending_name: ascending_name[0])
print(people_data)


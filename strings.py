course = "python is funny"
print(course[0:3])  # returns everything, between 0 and 3, excluding 3
print(course[1:])  # everything, excluding the first char

# formatted strings
first = 'Beray'
last = 'Syuleyman'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)

# string methods
print(len(msg))
print(msg.upper())
print(msg.find('P'))  # case sensitive
print(msg.replace('c', 'K'))  # case sensitive
print('for' in msg)


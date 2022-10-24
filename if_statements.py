is_hot = True
is_cold = False
if is_hot:
    print('Hot day')
elif is_cold:
    print('Cold day')
else:
    print('Test day')

print('Enjoy your day')

# logical operators
has_high_income = True
has_good_credit = True
criminal_record = False

# && -> and; || -> or; ! -> and not/ not

if has_high_income and has_good_credit and not criminal_record:
    print('My guy is rich')

# comparison operators -> >, <, ==, !=
temperature = 30

if temperature > 30:
    print("Hot day")
else:
    print("not")

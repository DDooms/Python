customer = {
    "name": "Beray Syuleyman",
    "age": 21,
    "is_verified": True
}
print(customer.get("name", "default"))  # if there is no such key, returns default

# phone number
phone = input("Phone: ")
phone_num = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""

for ch in phone:
    output += phone_num.get(ch, "!") + " "
print(output)

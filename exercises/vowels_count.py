def number_of_vowels(text):  # a, e, i, o, u
    count = 0
    for char in text:
        if char in "aeiou":
            count += 1
    return count


print(number_of_vowels("I am so confused!"))
print(number_of_vowels("gggggg"))
print(number_of_vowels("aaa"))

def caesar_cipher(string, offset):
    string_values = []
    encoded_values = []
    encoded_string = ""
    for letter in string:
        letter_value = ord(letter)
        string_values.append(letter_value)
    print(string_values)
    for value in string_values:
        value -= offset
        if value < 97:
            value = 122 - (96 - value)
        encoded_values.append(value)
    for value in encoded_values:
        letter = chr(value)
        encoded_string += letter
    return encoded_string


print(caesar_cipher("apple", 5))
print(caesar_cipher("hello", 3))
print(caesar_cipher("zzzz", 4))

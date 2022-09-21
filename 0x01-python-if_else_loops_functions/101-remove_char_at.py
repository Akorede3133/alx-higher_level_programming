#!/usr/bin/python3

def remove_char_at(str, n):
    arr = []
    string = ""
    if n < 0:
        return str
    else:
        for char in str:
            if char != str[n]:
                arr.append(char)
        for let in arr:
            string += let
    return string
print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun", 0))
print(remove_char_at("Python", -2))

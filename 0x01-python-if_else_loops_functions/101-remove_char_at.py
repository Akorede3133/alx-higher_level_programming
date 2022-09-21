#!/usr/bin/python3

def remove_char_at(str, n):
    arr = []
    string = ""
    if n < 0 or n > len(str) - 1:
        return str
    else:
        for char in str:
            if char != str[n]:
                arr.append(char)
        for let in arr:
            string += let
    return string

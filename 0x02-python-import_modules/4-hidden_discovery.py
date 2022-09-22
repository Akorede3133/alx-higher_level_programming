#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    string = []
    dir_str = dir(hidden_4)
    for elem in dir_str:
        if elem[0] != '_':
            string.append(elem)
    for elem in string:
        print(elem)

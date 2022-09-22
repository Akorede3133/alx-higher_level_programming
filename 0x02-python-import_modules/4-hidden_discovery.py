#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    str = dir(hidden_4)
    str = str[-3:]
    for elem in str:
        print(elem)

#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arglen = len(sys.argv) - 1
    if arglen == 0:
        print("0 arguments.")
    elif arglen == 1:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{arglen} arguments:")
        for elemIndex in range(1, arglen + 1):
            print(f"{elemIndex}: {sys.argv[elemIndex]}")
    #print(arglen)

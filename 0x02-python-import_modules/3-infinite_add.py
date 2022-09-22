#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arglen = len(sys.argv)
    res = 0;
    if arglen == 1:
        res += 0
    else:   
        for elemIndex in range(1, arglen):
            res += int(sys.argv[elemIndex])
    print(res)

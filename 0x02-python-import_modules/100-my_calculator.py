#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arglen = len(sys.argv)
    operators = ['+', '-', '*' '/']
    if (arglen < 4):
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if sys.argv[2] not in operators:
            print(f"Unknown operator. Available operators: +, -, *, and /")
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif sys.argv[2] == '-':
                print("{} + {} = {}".format(a, b, sub(a, b)))
            elif sys.argv[2] == '*':
                print("{} + {} = {}".format(a, b, mul(a, b)))
            elif sys.argv[2] == '/':
                print("{} + {} = {}".format(a, b, div(a, b)))


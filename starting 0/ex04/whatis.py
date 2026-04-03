import sys
argscount = sys.argv.__len__()

if argscount == 1:
    sys.exit()

try:
    assert (argscount == 2), 'more than one argument is provided'
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise ValueError("argument is not an integer")

    print("I'am Odd") if num % 2 else print("I'm Even")
except (AssertionError, ValueError) as e:
    print(f"AssertionError: {e}")
    sys.exit(1)

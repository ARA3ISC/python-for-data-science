import sys
from ft_filter import ft_filter


def filterstring(iter, n):
    '''it filters the string (keeping just the words
    that have len() more than n) and returned as list'''
    res = ft_filter(lambda w: len(w) > int(n), iter)
    print(res)


def main():
    '''the is the main function'''
    try:
        assert (
            len(sys.argv) == 3
            and sys.argv[2].isdigit()
        ), "the arguments are bad"
    except AssertionError as e:
        print(f'AssertionError: {e}')
        sys.exit(1)

    s = sys.argv[1]
    n = sys.argv[2]
    iterable = s.split()
    filterstring(iterable, n)


if __name__ == '__main__':
    main()

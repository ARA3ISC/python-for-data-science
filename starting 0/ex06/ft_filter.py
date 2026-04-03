
def startsWith_a(w):
    '''a helper function to test custon filter function'''
    return w.startswith("a")


def endsWith_a(w):
    '''a helper function to test custon filter function'''
    return w.endswith("a")


def ft_filter(func, iterable):
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true.

    If function is None, return the items that are true.
    """
    if not func:
        return iterable
    return [val for val in iterable if func(val)]


def main():
    '''the is the main function'''
    li = ["apple", "banana", "bnanas", "avocado", "cherry", "apricot"]
    res_custom = ft_filter(endsWith_a, li)
    res_builtin = filter(endsWith_a, li)
    print('result of custom filter function:  ', list(res_custom))
    print('result of built-in filter function:', list(res_builtin))
    print('\nTesting __doc__:\n')
    print('built-in filter docs :\n', res_builtin.__doc__)
    print('\n\ncustom filter docs :\n', ft_filter.__doc__)


if __name__ == '__main__':
    main()

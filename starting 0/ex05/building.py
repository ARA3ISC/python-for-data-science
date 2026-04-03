import sys


def countPunctuationMarks(s):
    '''printing punctuations marks'''
    puncs = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    count = 0
    for c in s:
        if c in puncs:
            count += 1

    print(f'{count} punctuation marks')


def countCharacters(s):
    '''printing characters count'''
    print(f'The text contains {len(s)} characters:')


def countSpaces(s):
    '''printing spaces count'''
    count = sum(True for c in s if c.isspace())
    print(f'{count} spaces')


def countUpperCase(s):
    '''printing uppercase characters count'''
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    print(f'{upper} upper letters')
    print(f'{lower} lower letters')


def countDigits(s):
    '''printing digits count'''
    count = sum(True for c in s if c.isnumeric())
    print(f'{count} digits')


def main():
    '''the is the main function'''

    if sys.argv.__len__() == 1:
        print('What is the text to count?')
        s = sys.stdin.read()

    else:
        try:
            assert sys.argv.__len__() == 2, 'It must be on argument'
            s = sys.argv[1]

        except AssertionError as e:
            print(f'AssertionError: {e}')
            sys.exit(1)

    countCharacters(s)
    countUpperCase(s)
    countPunctuationMarks(s)
    countSpaces(s)
    countDigits(s)


if __name__ == '__main__':
    main()

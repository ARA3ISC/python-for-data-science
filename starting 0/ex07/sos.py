import sys


def printMorseCode(s):
    NESTED_MORSE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",

        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",

        " ": "/"
    }

    morsed = ''
    for i, c in enumerate(s):
        morsed = morsed + NESTED_MORSE[c.upper()]
        morsed += ' ' if i != len(s) - 1 else ''

    print(morsed)


def main():
    try:
        assert (
            len(sys.argv) == 2
            and all(c.isalnum() or c == " " for c in sys.argv[1])
        ), "the arguments are bad"
    except AssertionError as e:
        print(f'AssertionError: {e}')
        sys.exit(1)
    s = sys.argv[1]
    printMorseCode(s)


if __name__ == '__main__':
    main()

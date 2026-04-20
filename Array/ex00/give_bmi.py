import numpy as np
    

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi = np.array(bmi)

    try:
        assert np.issubdtype(bmi.dtype, np.number), 'Invalid type'
    except AssertionError as e:
        print('Error: ', e)
        exit(1)

    return bmi > limit

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    h = np.array(height)
    w = np.array(weight)

    try:
        assert len(h) == len(w), 'Height and Weight list must have the same length'
        assert np.issubdtype(h.dtype, np.number) and np.issubdtype(w.dtype, np.number), 'Invalid type'
    except AssertionError as e:
        print('Error: ', e)
        exit(1)

    return (w / h**2).tolist()


def main():
    # print(give_bmi([3, 2, 4], [3, 1, 5]))
    print(apply_limit([2, 4], 3))

if __name__ == '__main__':
    main()
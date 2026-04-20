import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        arr = np.array(family)
        assert arr.ndim == 2, 'Input must be a 2D list with consistent row sizes'
        print(f'My shape is : {arr.shape}')
        arr = arr[start:end]
        print(f'My new shape is : {arr.shape}')
    except (AssertionError, ValueError) as e:
        print(f'Error: {e}')
        exit(1)
    return arr.tolist()

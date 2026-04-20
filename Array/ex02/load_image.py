from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    img = Image.open(path)
    arr = np.array(img)
    print(arr.shape)
    return arr

np.set_printoptions(threshold=5)
print(ft_load('landscape.jpg'))
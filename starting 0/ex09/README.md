# ft_package

A simple package that counts occurrences of items in lists.

## Installation
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
OR
pip install ./dist/ft_package-0.0.1-py3-none-any.whl 
```

## Usage
```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

## Author

Mohamed Aneddame (aka Arabi) (aneddame.contact@gmail.com)

## License

MIT
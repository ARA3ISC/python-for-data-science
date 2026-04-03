# test_package.py
from ft_package import count_in_list

# Test 1
result = count_in_list(["toto", "tata", "toto"], "toto")
assert result == 2, f"Expected 2, got {result}"
print("✓ Test 1 passed")

# Test 2
result = count_in_list(["toto", "tata", "toto"], "tutu")
assert result == 0, f"Expected 0, got {result}"
print("✓ Test 2 passed")

print("\nAll tests passed!")

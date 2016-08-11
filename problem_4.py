from string import is_palindrome

# List all factors
factors = [i for i in range(100, 999)]

# Now loop through all combinations of factors
palindrome_factors = []
best_palindrome = None
for f1 in factors:
    for f2 in factors:
        if f2 >= f1:
            product = f1 * f2
            if (best_palindrome is None or product > best_palindrome) and is_palindrome(str(product)):
                best_palindrome = product
                palindrome_factors = [f1, f2]

print(best_palindrome)

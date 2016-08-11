n = 100

# Make to sums, one sums of squares and one square of sums
s1 = 0
s2 = 0
for i in range(1, n + 1):
    s1 += i
    s2 += i ** 2

print(s1 ** 2 - s2)

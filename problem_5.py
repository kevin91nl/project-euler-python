from collections import defaultdict

import math

from counting import get_counts
from integer.primes import find_prime_factors

# Find all smallest prime powers
powers = defaultdict(int)
for i in range(1, 21):
    counts = get_counts(find_prime_factors(i))
    for prime in counts:
        powers[prime] = max(powers[prime], counts[prime])

# And now calculate the LCM
lcm = 1
for factor in powers:
    lcm *= int(math.pow(factor, powers[factor]))
print(lcm)

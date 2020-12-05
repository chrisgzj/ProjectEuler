# Problem 265
# https://projecteuler.net/problem=265
# Description:
# 2N binary digits can be placed in a circle so that all the N-digit clockwise subsequences are distinct.
# For N=3, two such circular arrangements are possible, ignoring rotations:
# For the first arrangement, the 3-digit subsequences, in clockwise order, are: 000, 001, 010, 101, 011, 111, 110 and 100.
# Each circular arrangement can be encoded as a number by concatenating the binary digits starting with the subsequence of all zeros as the most significant bits and proceeding clockwise. The two arrangements for N=3 are thus represented as 23 and 29:
# 00010111 2 = 23
# 00011101 2 = 29
# Calling S(N) the sum of the unique numeric representations, we can see that S(3) = 23 + 29 = 52.
# Find S(5).
from datetime import datetime
combinations = []
def all_combinations(n, current_string = ''):
    """Generates recursively all possible combinations of digits 1 and 0 with length N"""
    global combinations
    if n == 0:
        combinations.append(current_string)
        return
    all_combinations(n - 1, current_string + '0')
    all_combinations(n - 1, current_string + '1')

print(datetime.now())
all_combinations(32)
print(len(combinations))
print(datetime.now())

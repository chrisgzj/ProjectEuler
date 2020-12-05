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
import json

candidates = []

def check_subsequence_repetition(current_string_original, r, string_complete):
    """Checks wether a string contains duplicated subsequences of length r.
    Returns False if a repeated subsequence is found.
    If string_complete is True, it also checks for modular repetitions appending the first r
    digits to the end of the string"""
    subsequences = []
    if string_complete:
        current_string = current_string_original + current_string_original[:r]
    else:
        current_string = current_string_original
    for index in range(0, len(current_string) - r):
        subseq = current_string[index: index + r]
        if subseq in subsequences:
            return False
        else:
            subsequences.append(subseq)
    return True

def all_candidates(n, r, current_string = '', restrict = True):
    """Generates recursively all possible combinations of digits 1 and 0 with length N,
    discarding on each step those that already violate the condition of no repeated subsequences
    n is an integer that represents the length of the sequence
    r is an integer thet represents the length of the subsequence
    restrict is a boolean that represents if candidates with repeated subsequences are to be discarded"""
    global candidates
    if len(current_string) > r and n > 0 and restrict:
        if not check_subsequence_repetition(current_string, r, False):
            return
    if n == 0:
        if check_subsequence_repetition(current_string, r, True):
            candidates.append(current_string)
        return
    all_candidates(n - 1, r, current_string + '0', restrict)
    all_candidates(n - 1, r, current_string + '1', restrict)


def main():
    print(datetime.now())
    all_candidates(32, 5)
    print(len(candidates))
    with open('candidates_p265.json', 'w') as outfile:
        json.dump(candidates, outfile)
    print(datetime.now())



# 1526656 Without filtering last character
# 742208 Without checking modular
# 65536 Checking modular

# 4 minutes to run all_candidates

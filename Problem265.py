# Problem 265
# https://projecteuler.net/problem=265
# Difficulty rating: 40%
# Status: Solved inefficiently (takes aprox. 5 minutes to run).

# Description of the problem:
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

def basic_rotate(candidate):
    """Removes all the zeros at the end of candidate and adds them at the beginning of itself
    Removes all ones at the begenning and adds them to the end"""
    digits = list(candidate)
    for digit_index in range(len(candidate)):
        if digits[len(digits)-1] == "0": # Always the last because the list is changed inside the loop.
            digits.insert(0, digits.pop(len(digits)-1))
        else:
            break
    for digit_index in range(len(candidate)):
        if digits[0] == "1": # Always the first because the list is changed inside the loop.
            digits.append(digits.pop(0))
        else:
            break
    return "".join(digits)

def eliminate_rotations(with_rotations):
    """Eliminates strings that represent a rotation of another solution.
    Keeps the repetition that has the most number of ceros to the left"""
    rotated = []
    for candidate in with_rotations:
        rotated_candidate = basic_rotate(candidate)
        if rotated_candidate not in rotated:
            rotated.append(rotated_candidate)
    # After keeping only the candidates that comply with the basic rotation, we still have to exclude those
    # repetitions in which both cases comply with having a cero at the beginning and a 1 at the end.
    # For that, we check every possible rotation of every candiadate and, if present in rotated, we keep
    # the smallest one, since it is the one with the most zeros at the left.
    # Doing this from the beginning would be too costly in processing time.
    for candidate in rotated:
        for rotate_size in range(1, len(candidate)):
            rotated_cand_2 = candidate[rotate_size:] + candidate[:rotate_size]
            if rotated_cand_2 in rotated:
                if int(rotated_cand_2, 2) < int(candidate, 2):
                    rotated.remove(candidate)
                else:
                    rotated.remove(rotated_cand_2)

    return rotated


def main():
    print(datetime.now())
    global candidates
    candidates = []
    all_candidates(8, 3)
    # with open('candidates_p265.json', 'w') as outfile:
    #     json.dump(candidates, outfile)
    # with open('candidates_p265.json', 'r') as infile:
    #     candidates = json.load(infile)
    binary_solutions = eliminate_rotations(candidates)
    integer_sum = sum([int(bin, 2) for bin in binary_solutions])
    print(integer_sum)
    print(datetime.now())

main()

# 1526656 candidates without filtering last character
# 742208 candidates Without checking modular repetition
# 65536 candidates checking modular
# 32768 solutions without basic rotations

# 5 minutes to run all_candidates, 1 minute to run the rest.
# Final solution: 209110240768


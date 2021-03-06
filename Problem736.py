# Problem 736
# https://projecteuler.net/problem=736

from datetime import datetime
def find_smallest_odd_path(r, s, a, b, limit, counter = 1):
    """Recursive function to find the smallest path to equality that has an odd length.
    The funcion explores both the path generated by the r and the functions on each step and
    compares them to return the one with smallest length"""
    if counter > limit:
        return 0, 0, limit * 1000 # The returned counter when the limit was reached needs to
        # be greater than the possible real counter and easy to be identified as a failure.
    if a == b and (counter % 2 != 0 or True):
        print (counter, a, b)
        return a, b, counter
    r_a, r_b = r(a,b)
    r_side_a, r_side_b, r_side_counter = find_smallest_odd_path(r, s, r_a, r_b, limit, counter+1)
    s_a, s_b = s(a,b)
    s_side_a, s_side_b, s_side_counter = find_smallest_odd_path(r, s, s_a, s_b, limit, counter + 1)
    if r_side_counter <= s_side_counter:
        if r_side_counter < 1000:
            print (counter, a, b)
        return r_side_a, r_side_b, r_side_counter
    if s_side_counter < 1000: #Option to visualize successful even paths.
        print(counter, a, b)
    return s_side_a, s_side_b, s_side_counter


def main():
    def lattice_r(x,y):
        return x + 1, 2 * y

    def lattice_s(x,y):
        return 2 * x, y + 1

    for limit in range(15, 16): # Greedy approach to increasing limit.
        print(f"Searching for limit {limit}:")
        print(datetime.now())
        a, b, counter = find_smallest_odd_path(lattice_r, lattice_s, 45, 90, limit)
        if counter <= limit:
            print(a,b,counter)
        else:
            print("Not found")

main()


# Find the unique
"""Recursion design"""

import sys


def summation(low, high):
    """return sum of integers"""
    if low == high:
        return high
    else:
        return low + summation(low + 1, high)


def summation2(low, high):
    """Returns the summation of the integers
    from low to high.
    Precondition: low <= high."""
    total = 0
    for number in range(low, high + 1):
        total += number
    return total


def summation3(low, high, total = 0):
    """Returns the summation of the integers
    from low to high.
    Precondition: low <= high."""
    if low > high:
        return total
    else:
        return summation3(low + 1, high, low + total)

def main(low=6, high=4):
    if len(sys.argv) == 3:
        low = int(sys.argv[1])
        high = int(sys.argv[2])

    print("The sum of", low, "and", high, "is", summation(low, high))


if __name__ == '__main__':
    main()

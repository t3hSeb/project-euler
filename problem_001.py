"""Problem 1.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples(divisor_a: int, divisor_b: int, max_range: int = 100):
    """Find sum of multiples of two divisors up to a maximum.

    Calculate the sum of all integers that are multiples of two integers.

    :param divisor_a: first divisor
    :param divisor_b: second divisor
    :param max_range: maximum integer up to which we find the multiples of the two divisors
    :return: sum of all multiples of the two divisors up to max_range
    """
    # Check we have at least the maximum of our multiples
    assert max_range >= max(divisor_a, divisor_b), \
        f"Maximum range must be greater than or equal to {max(divisor_a, divisor_b)}"

    def _check_integers(parameter):
        """Check if parameters are integers

        :param parameter: parameters that should be an integer to be checked
        """
        assert parameter.__class__ == int, f"Parameter '{parameter}' must be an integer!"

    _check_integers(divisor_a)
    _check_integers(divisor_b)
    _check_integers(max_range)

    multiples = []
    for i in range(0, max_range):
        if (i % divisor_a == 0) or (i % divisor_b == 0):
            multiples.append(i)

    multiples = list(set(multiples))
    total = sum(multiples)
    return multiples, total


if __name__ == "__main__":
    _, sum_of_multiples = sum_multiples(3, 5, 1000)
    print(sum_of_multiples)
    print(_)

def calculate_product(factors):
    """
    Given a list of integers, calculate the product

    :param factors: A list of integers
    :return: Suppose the list consists of integers k_1, ..., k_n, then the result is k_1 * ... * k_n
    """
    n = 1
    for factor in factors:
        n *= factor
    return n

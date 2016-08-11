def get_counts(l):
    """
    This method computes a dictionary with keys all unique elements in the given list and where the values are the number
    of occurrences of the given key in the list.

    :param l: The list
    :return: The counts
    """
    return {k: sum([1 for element in l if element == k]) for k in l}

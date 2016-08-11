def is_palindrome(s):
    """
    Test whether a string s is a palindrome. That means, s == get_reverse(s).

    :param s: A string
    :return: True if s is a palindrome, False otherwise
    """
    return s == get_reverse(s)


def get_reverse(s):
    """
    Given a string consisting of characters s_1, s_2, ... s_n, get its reverse: s_n, ..., s_2, s_1.

    :param s: The string
    :return: The reversed string
    """
    return ''.join([s[-i - 1] for (i, a) in enumerate(s)])
